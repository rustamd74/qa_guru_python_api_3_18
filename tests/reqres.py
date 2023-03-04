import pytest
from pytest_voluptuous import S

from schemas.user import create_single_user, login_successful, register_single_user, unregister_single_user, \
    login_unsuccessful


def test_register_successful(regres_api):
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    register_user = regres_api.post('api/register', data=data)

    assert register_user.status_code == 200
    assert S(register_single_user) == register_user.json()
    assert register_user.json()['id']
    assert register_user.json()['token']


def test_register_unsuccessful(regres_api):
    data = {
        "email": "sydney@fife"
    }
    register_user = regres_api.post("api/register", data=data)

    assert register_user.status_code == 400
    assert S(unregister_single_user) == register_user.json()


def test_login_successful(regres_api):
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    login_user = regres_api.post("api/login", data=data)
    assert login_user.status_code == 200
    assert S(login_successful) == login_user.json()
    assert login_user.json()['token']


def test_login_unsuccessful(regres_api):
    data = {
        "email": "peter@klaven"
    }
    unlogin_user = regres_api.post("api/login", data=data)
    assert unlogin_user.status_code == 400
    assert S(login_unsuccessful) == unlogin_user.json()


def test_create(regres_api):
    data = {
        "name": "morpheus",
        "job": "leader",
        "id": "778",
        "createdAt": "2023-02-26T14:29:35.691Z"
    }
    create_user = regres_api.post("api/users", data=data)
    assert create_user.status_code == 201
    assert S(create_single_user) == create_user.json()


def test_delete(regres_api):
    delete_user = regres_api.delete("api/users/2")

    assert delete_user.status_code == 204
