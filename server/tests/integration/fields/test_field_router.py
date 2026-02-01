def _create_field(client):
    response = client.post(
        '/api/v1/fields/',
        json={
            'form_id': 1,
            'slug': 'campo_teste',
            'label': 'Campo Teste',
            'type': 1,
            'order': 1,
            'readonly': False,
            'observation': 'Obs',
            'optional': 'N',
            'grid': 'col-12',
            'size': 10,
            'mask': None,
            'placeholder': 'Digite aqui',
        },
    )
    assert response.status_code == 201
    return response.json()


def test_create_field(client):
    data = _create_field(client)

    assert data['id'] is not None
    assert data['slug'] == 'campo_teste'
    assert data['label'] == 'Campo Teste'
    assert data['type'] == 'Texto' or isinstance(data['type'], str)
    assert data['order'] == 1
    assert data['readonly'] is False


def test_list_fields(client):
    _create_field(client)
    _create_field(client)

    response = client.get('/api/v1/fields/')
    assert response.status_code == 200

    body = response.json()

    assert 'items' in body
    assert body['total_items'] == 2
    assert len(body['items']) == 2


def test_get_field_success(client):
    created = _create_field(client)
    field_id = created['id']

    response = client.get(f'/api/v1/fields/{field_id}')
    assert response.status_code == 200

    data = response.json()
    assert data['id'] == field_id
    assert data['label'] == 'Campo Teste'


def test_get_field_not_found(client):
    response = client.get('/api/v1/fields/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Campo não encontrado'


def test_update_field(client):
    created = _create_field(client)
    field_id = created['id']

    response = client.put(
        f'/api/v1/fields/{field_id}',
        json={
            'form_id': 1,
            'slug': 'campo_atualizado',
            'label': 'Campo Atualizado',
            'type': 2,
            'order': 2,
            'readonly': True,
            'observation': 'Atualizado',
            'optional': 'S',
            'grid': 'col-6',
            'size': 20,
            'mask': None,
            'placeholder': 'Novo texto',
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['slug'] == 'campo_atualizado'
    assert data['label'] == 'Campo Atualizado'
    assert data['order'] == 2
    assert data['readonly'] is True


def test_update_field_not_found(client):
    response = client.put(
        '/api/v1/fields/999',
        json={
            'form_id': 1,
            'slug': 'x',
            'label': 'x',
            'type': 1,
            'order': 1,
            'readonly': False,
        },
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Campo não encontrado'


def test_patch_field(client):
    created = _create_field(client)
    field_id = created['id']

    response = client.patch(
        f'/api/v1/fields/{field_id}',
        json={
            'label': 'Patch Atualizado',
            'order': 99,
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data['label'] == 'Patch Atualizado'
    assert data['order'] == 99


def test_patch_field_not_found(client):
    response = client.patch(
        '/api/v1/fields/999',
        json={'label': 'X'},
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Campo não encontrado'


def test_delete_field(client):
    created = _create_field(client)
    field_id = created['id']

    response = client.delete(f'/api/v1/fields/{field_id}')
    assert response.status_code == 204


def test_delete_field_not_found(client):
    response = client.delete('/api/v1/fields/999')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Campo não encontrado'
