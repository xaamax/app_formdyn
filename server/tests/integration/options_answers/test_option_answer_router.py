def _create_form(client):
    response = client.post(
        '/api/v1/forms/',
        json={
            'name': 'Form Teste',
            'order': 1,
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


def _create_option_answers(client):
    form = _create_form(client)
    answer = _create_answers(client)

    response = client.post(
        '/api/v1/options_answers/',
        json={
            'form_id': form['id'],
            'answer_id': answer['id'],
            'order': 1,
        },
    )
    assert response.status_code == 201
    return response.json()


def test_create_option_answers(client):
    data = _create_option_answers(client)

    assert data['id'] is not None
    assert 'form_name' in data
    assert 'answer_description' in data


def test_list_option_answers(client):
    _create_option_answers(client)
    _create_option_answers(client)

    response = client.get('/api/v1/options_answers/')
    assert response.status_code == 200

    body = response.json()

    assert 'items' in body
    assert body['total_items'] == 2
    assert len(body['items']) == 2


def test_get_option_answers_success(client):
    created = _create_option_answers(client)
    option_answer_id = created['id']

    response = client.get(f'/api/v1/options_answers/{option_answer_id}')
    assert response.status_code == 200

    data = response.json()
    assert data['id'] == option_answer_id


def test_get_option_answers_not_found(client):
    response = client.get('/api/v1/options_answers/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Opção de Resposta não encontrada'


def test_update_option_answers(client):
    created = _create_option_answers(client)
    option_answer_id = created['id']

    new_form = _create_form(client)
    new_answer = _create_answers(client)

    response = client.put(
        f'/api/v1/options_answers/{option_answer_id}',
        json={
            'form_id': new_form['id'],
            'answer_id': new_answer['id'],
            'order': 10,
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['id'] == option_answer_id
    assert data['form_name'] == new_form['name']
    assert data['answer_description'] == new_answer['description']


def test_update_option_answers_not_found(client):
    response = client.put(
        '/api/v1/options_answers/999',
        json={
            'form_id': 1,
            'answer_id': 1,
            'order': 1,
        },
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Opção de Resposta não encontrada'


def test_patch_option_answers(client):
    created = _create_option_answers(client)
    option_answer_id = created['id']

    response = client.patch(
        f'/api/v1/options_answers/{option_answer_id}',
        json={
            'order': 99,
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['id'] == option_answer_id


def test_patch_option_answers_not_found(client):
    response = client.patch(
        '/api/v1/options_answers/999',
        json={'order': 5},
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Opção de Resposta não encontrada'


def test_delete_option_answers(client):
    created = _create_option_answers(client)
    option_answer_id = created['id']

    response = client.delete(f'/api/v1/options_answers/{option_answer_id}')
    assert response.status_code == 204


def test_delete_option_answers_not_found(client):
    response = client.delete('/api/v1/options_answers/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Opção de Resposta não encontrada'
