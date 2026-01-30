def test_create_form(client):
    response = client.post(
        '/api/v1/forms/',
        json={'name': 'Form Teste', 'type': 1},
    )

    assert response.status_code == 201
    data = response.json()

    assert data['name'] == 'Form Teste'
    assert data['type'] == 'Formulário Ensino Fundamental'


def test_list_forms(client):
    client.post('/api/v1/forms/', json={'name': 'A', 'type': 1})
    client.post('/api/v1/forms/', json={'name': 'B', 'type': 2})

    response = client.get('/api/v1/forms/')
    assert response.status_code == 200

    data = response.json()
    assert len(data['forms']) == 2


def test_get_form_success(client):
    create = client.post(
        '/api/v1/forms/',
        json={'name': 'Get Test', 'type': 1},
    )
    form_id = create.json()['id']

    response = client.get(f'/api/v1/forms/{form_id}')

    assert response.status_code == 200
    data = response.json()

    assert data['name'] == 'Get Test'
    assert data['type'] == 'Formulário Ensino Fundamental'


def test_get_form_not_found(client):
    response = client.get('/api/v1/forms/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Form not found'


def test_update_form(client):
    create = client.post('/api/v1/forms/', json={'name': 'Old', 'type': 1})
    form_id = create.json()['id']

    response = client.put(
        f'/api/v1/forms/{form_id}',
        json={'name': 'New', 'type': 2},
    )

    assert response.status_code == 201
    assert response.json()['name'] == 'New'
    assert response.json()['type'] == 'Formulário Ensino Médio'


def test_update_form_not_found(client):
    response = client.put(
        '/api/v1/forms/999',
        json={'name': 'X', 'type': 1},
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Form not found'


def test_patch_form(client):
    create = client.post('/api/v1/forms/', json={'name': 'Patch', 'type': 1})
    form_id = create.json()['id']

    response = client.patch(
        f'/api/v1/forms/{form_id}',
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
    assert response.json()['detail'] == 'Form not found'


def test_delete_form(client):
    create = client.post('/api/v1/forms/', json={'name': 'Delete', 'type': 1})
    form_id = create.json()['id']

    response = client.delete(f'/api/v1/forms/{form_id}')

    assert response.status_code == 204


def test_delete_form_not_found(client):
    response = client.delete('/api/v1/forms/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Form not found'
