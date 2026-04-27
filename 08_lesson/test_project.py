
from ProjectApi import ProjectApi

api = ProjectApi("https://ru.yougile.com")


def test_add_project_positive():
    name = "My test project"
    resp, result = api.create_project(name)
    assert resp.status_code == 201
    assert result["id"] is not None


def test_edit_positive():
    name = "My first project"
    resp, json_result = api.create_project(name)
    create_id = json_result['id']
    new_name = "My_project"
    resp, edited = api.edit_project(new_name, create_id)
    assert resp.status_code == 200
    assert edited['id'] == create_id


def test_get_project_id_positive():
    name = "My second project"
    resp, json_result = api.create_project(name)
    create_id = json_result['id']
    resp, project = api.get_project(create_id)
    assert resp.status_code == 200
    assert project['title'] == name


def test_add_project_negative():
    name = ""
    resp, body = api.create_project(name)
    assert resp.status_code == 400
    assert body['error'] == 'Bad Request'


def test_edit_negative():
    name = "My first project"
    resp, json_result = api.create_project(name)
    create_id = json_result['id']
    new_name = ""
    resp, edited = api.edit_project(new_name, create_id)
    assert resp.status_code == 400
    assert edited['error'] == 'Bad Request'


def test_get_project_id_negative():
    name = "My second project"
    api.create_project(name)
    id = "123456789"
    resp, project = api.get_project(id)
    assert resp.status_code == 404
    assert project['error'] == 'Not Found'
