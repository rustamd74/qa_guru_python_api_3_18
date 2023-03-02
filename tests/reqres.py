from pytest_voluptuous import S

from schemas.user import create_single_user, login_successful, register_single_user, unregister_single_user, \
    login_unsuccessful


def test_register_successful(regres):
    register_user = regres.post('api/register', {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })

    assert register_user.status_code == 200
    assert S(register_single_user) == register_user.json()
    assert register_user.json()['id']
    assert register_user.json()['token']


def test_register_unsuccessful(regres):
    register_user = regres.post("api/register", {
        "email": "sydney@fife"
    })

    assert register_user.status_code == 400
    assert S(unregister_single_user) == register_user.json()


def test_login_successful(regres):
    login_user = regres.post("api/login", {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    })
    assert login_user.status_code == 200
    assert S(login_successful) == login_user.json()
    assert login_user.json()['token']


def test_login_unsuccessful(regres):
    unlogin_user = regres.post("api/login", {
        "email": "peter@klaven"
    })
    assert unlogin_user.status_code == 400
    assert S(login_unsuccessful) == unlogin_user.json()


def test_create(regres):
    create_user = regres.post("api/users", {
        "name": "morpheus",
        "job": "leader",
        "id": "778",
        "createdAt": "2023-02-26T14:29:35.691Z"
    })
    assert create_user.status_code == 201
    assert S(create_single_user) == create_user.json()


def test_delete(regres):
    delete_user = regres.delete("api/users/2")

    assert delete_user.status_code == 204
