def _create_answers_form(client):
    response = client.post(
        '/api/v1/answers_forms/',
        json={
            'description': 'teste_description',
            'legend': 'teste_legend',
            'order': 1,
            'only_legend': False,
            'color': '#FFFFF',
            'background': '#FFFFF',
        },
    )
    assert response.status_code == 201
    return response.json()


def test_create_answers_form(client):
    data = _create_answers_form(client)

    assert data['id'] is not None
    assert data['description'] == 'teste_description'
    assert data['legend'] == 'teste_legend'
    assert data['order'] == 1
    assert data['only_legend'] is False
    assert data['color'] == '#FFFFF'
    assert data['background'] == '#FFFFF'


def test_list_answers_forms(client):
    _create_answers_form(client)
    _create_answers_form(client)

    response = client.get('/api/v1/answers_forms/')
    assert response.status_code == 200

    body = response.json()

    assert 'items' in body
    assert body['total_items'] == 2
    assert len(body['items']) == 2


def test_get_answers_form_success(client):
    created = _create_answers_form(client)
    answers_form_id = created['id']

    response = client.get(f'/api/v1/answers_forms/{answers_form_id}')
    assert response.status_code == 200

    data = response.json()
    assert data['id'] == answers_form_id
    assert data['description'] == 'teste_description'


def test_get_answers_form_not_found(client):
    response = client.get('/api/v1/answers_forms/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'AnswerForm not found'


def test_update_answers_form(client):
    created = _create_answers_form(client)
    answers_form_id = created['id']

    response = client.put(
        f'/api/v1/answers_forms/{answers_form_id}',
        json={
            'description': 'teste_description',
            'legend': 'teste_legend',
            'order': 1,
            'only_legend': False,
            'color': '#FFFFF',
            'background': '#FFFFF',
        },
    )

    assert response.status_code == 201
    data = response.json()

    assert data['id'] is not None
    assert data['description'] == 'teste_description'
    assert data['legend'] == 'teste_legend'


def test_update_answers_form_not_found(client):
    response = client.put(
        '/api/v1/answers_forms/999',
        json={
            'description': 'teste_description',
            'legend': 'teste_legend',
            'order': 1,
            'only_legend': False,
            'color': '#FFFFF',
            'background': '#FFFFF',
        },
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'AnswerForm not found'


def test_patch_answers_form(client):
    created = _create_answers_form(client)
    answers_form_id = created['id']

    response = client.patch(
        f'/api/v1/answers_forms/{answers_form_id}',
        json={
            'description': 'teste_description',
            'order': 99,
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['description'] == 'teste_description'
    assert data['order'] == 99


def test_patch_answers_form_not_found(client):
    response = client.patch(
        '/api/v1/answers_forms/999',
        json={'description': 'X'},
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'AnswerForm not found'


def test_delete_answers_form(client):
    created = _create_answers_form(client)
    answers_form_id = created['id']

    response = client.delete(f'/api/v1/answers_forms/{answers_form_id}')
    assert response.status_code == 204


def test_delete_answers_form_not_found(client):
    response = client.delete('/api/v1/answers_forms/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'AnswerForm not found'
