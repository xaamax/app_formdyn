def _create_form(client, name='Form', type=1):
    response = client.post(
        '/api/v1/forms/',
        json={'name': name, 'type': type},
    )
    assert response.status_code == 201
    return response.json()


def test_create_form(client):
    data = _create_form(client, 'Form Teste', 1)

    assert data['name'] == 'Form Teste'
    assert data['type'] == 'Formulário Ensino Fundamental'


def test_list_forms(client):
    _create_form(client, 'Form A', 1)
    _create_form(client, 'Form B', 2)

    response = client.get('/api/v1/forms/?page_number=1&page_size=10')
    assert response.status_code == 200

    body = response.json()
    assert 'items' in body
    assert body['total_items'] == 2
    assert len(body['items']) == 2


def test_get_form_success(client):
    created = _create_form(client, 'Get Test', 1)

    response = client.get(f'/api/v1/forms/{created["id"]}')
    assert response.status_code == 200

    data = response.json()
    assert data['name'] == 'Get Test'
    assert data['type'] == 'Formulário Ensino Fundamental'


def test_get_form_not_found(client):
    response = client.get('/api/v1/forms/999')

    assert response.status_code == 404

    body = response.json()
    assert body['status_code'] == 404
    assert body['detail'] == 'Formulário não encontrado'


def test_update_form(client):
    created = _create_form(client, 'Old', 1)

    response = client.put(
        f'/api/v1/forms/{created["id"]}',
        json={'name': 'New', 'type': 2},
    )

    assert response.status_code == 200
    data = response.json()

    assert data['name'] == 'New'
    assert data['type'] == 'Formulário Ensino Médio'


def test_update_form_not_found(client):
    response = client.put(
        '/api/v1/forms/999',
        json={'name': 'X', 'type': 1},
    )

    assert response.status_code == 404

    body = response.json()
    assert body['status_code'] == 404
    assert body['detail'] == 'Formulário não encontrado'


def test_patch_form(client):
    created = _create_form(client, 'Patch', 1)

    response = client.patch(
        f'/api/v1/forms/{created["id"]}',
        json={'name': 'Patch Atualizado'},
    )

    assert response.status_code == 200
    assert response.json()['name'] == 'Patch Atualizado'


def test_patch_form_not_found(client):
    response = client.patch(
        '/api/v1/forms/999',
        json={'name': 'X'},
    )

    assert response.status_code == 404

    body = response.json()
    assert body['status_code'] == 404
    assert body['detail'] == 'Formulário não encontrado'


def test_delete_form(client):
    created = _create_form(client, 'Delete', 1)

    response = client.delete(f'/api/v1/forms/{created["id"]}')
    assert response.status_code == 204


def test_delete_form_not_found(client):
    response = client.delete('/api/v1/forms/999')

    assert response.status_code == 404

    body = response.json()
    assert body['status_code'] == 404
    assert body['detail'] == 'Formulário não encontrado'
