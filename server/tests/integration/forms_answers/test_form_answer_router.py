def _create_form(client):
    response = client.post(
        '/api/v1/forms/',
        json={
            'name': 'Form Teste',
            'type': 1,
        },
    )
    assert response.status_code == 201
    return response.json()


def _create_answers(client):
    response = client.post(
        '/api/v1/answers/',
        json={
            'description': 'Resposta Teste',
            'legend': 'Legenda',
            'order': 1,
            'only_legend': False,
            'color': '#FFFFF',
            'background': '#FFFFF',
        },
    )
    assert response.status_code == 201
    return response.json()


def _create_forms_answers(client):
    form = _create_form(client)
    answer = _create_answers(client)

    response = client.post(
        '/api/v1/forms_answers/',
        json={
            'form_id': form['id'],
            'answer_id': answer['id'],
            'value': 'Teste',
        },
    )
    assert response.status_code == 201
    return response.json()


def test_create_forms_answers(client):
    data = _create_forms_answers(client)

    assert data['id'] is not None
    assert data['form_id'] == 1
    assert data['answer_id'] == 1
    assert data['value'] == 'Teste'


def test_list_forms_answers(client):
    _create_forms_answers(client)
    _create_forms_answers(client)

    response = client.get('/api/v1/forms_answers/')
    assert response.status_code == 200

    body = response.json()

    assert 'items' in body
    assert body['total_items'] == 2
    assert len(body['items']) == 2


def test_get_forms_answers_success(client):
    created = _create_forms_answers(client)
    id = created['id']

    response = client.get(f'/api/v1/forms_answers/{id}')
    assert response.status_code == 200

    data = response.json()
    assert data['id'] == id


def test_get_forms_answers_not_found(client):
    response = client.get('/api/v1/forms_answers/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Resposta de Formulário não encontrada'


def test_update_forms_answers(client):
    created = _create_forms_answers(client)
    id = created['id']

    new_form = _create_form(client)
    new_answer = _create_answers(client)

    response = client.put(
        f'/api/v1/forms_answers/{id}',
        json={
            'form_id': new_form['id'],
            'answer_id': new_answer['id'],
            'value': 'Teste',
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['id'] == id
    assert data['form_id'] == new_form['id']
    assert data['answer_id'] == new_answer['id']


def test_update_forms_answers_not_found(client):
    response = client.put(
        '/api/v1/forms_answers/999',
        json={
            'form_id': 1,
            'answer_id': 1,
            'value': 'Teste',
        },
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Resposta de Formulário não encontrada'


def test_patch_forms_answers(client):
    created = _create_forms_answers(client)
    id = created['id']

    response = client.patch(
        f'/api/v1/forms_answers/{id}',
        json={
            'value': 'Teste',
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['id'] == id


def test_patch_forms_answers_not_found(client):
    response = client.patch(
        '/api/v1/forms_answers/999',
        json={'value': 'Teste'},
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Resposta de Formulário não encontrada'


def test_delete_forms_answers(client):
    created = _create_forms_answers(client)
    id = created['id']

    response = client.delete(f'/api/v1/forms_answers/{id}')
    assert response.status_code == 204


def test_delete_forms_answers_not_found(client):
    response = client.delete('/api/v1/forms_answers/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Resposta de Formulário não encontrada'
