def _create_answers(client):
    response = client.post(
        '/api/v1/answers/',
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


def test_create_answers(client):
    data = _create_answers(client)

    assert data['id'] is not None
    assert data['description'] == 'teste_description'
    assert data['legend'] == 'teste_legend'
    assert data['order'] == 1
    assert data['only_legend'] is False
    assert data['color'] == '#FFFFF'
    assert data['background'] == '#FFFFF'


def test_list_answers(client):
    _create_answers(client)
    _create_answers(client)

    response = client.get('/api/v1/answers/')
    assert response.status_code == 200

    body = response.json()

    assert 'items' in body
    assert body['total_items'] == 2
    assert len(body['items']) == 2


def test_get_answers_success(client):
    created = _create_answers(client)
    answers_id = created['id']

    response = client.get(f'/api/v1/answers/{answers_id}')
    assert response.status_code == 200

    data = response.json()
    assert data['id'] == answers_id
    assert data['description'] == 'teste_description'


def test_get_answers_not_found(client):
    response = client.get('/api/v1/answers/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Resposta não encontrada'


def test_update_answers(client):
    created = _create_answers(client)
    answers_id = created['id']

    response = client.put(
        f'/api/v1/answers/{answers_id}',
        json={
            'description': 'teste_description',
            'legend': 'teste_legend',
            'order': 1,
            'only_legend': False,
            'color': '#FFFFF',
            'background': '#FFFFF',
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['id'] is not None
    assert data['description'] == 'teste_description'
    assert data['legend'] == 'teste_legend'


def test_update_answers_not_found(client):
    response = client.put(
        '/api/v1/answers/999',
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
    assert response.json()['detail'] == 'Resposta não encontrada'


def test_patch_answers(client):
    created = _create_answers(client)
    answers_id = created['id']

    response = client.patch(
        f'/api/v1/answers/{answers_id}',
        json={
            'description': 'teste_description',
            'order': 99,
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['description'] == 'teste_description'
    assert data['order'] == 99


def test_patch_answers_not_found(client):
    response = client.patch(
        '/api/v1/answers/999',
        json={'description': 'X'},
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Resposta não encontrada'


def test_delete_answers(client):
    created = _create_answers(client)
    answers_id = created['id']

    response = client.delete(f'/api/v1/answers/{answers_id}')
    assert response.status_code == 204


def test_delete_answers_not_found(client):
    response = client.delete('/api/v1/answers/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Resposta não encontrada'
