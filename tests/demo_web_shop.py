import os

from selene import have

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


def test_auth_login(auth_user):
    auth_user.open('')
    auth_user.element('.account').should(have.text(LOGIN))


def test_add_to_cart(auth_user, demoshop):
    demoshop.get('/notebooks')
    auth_user.element('.button-2 ').click()


def test_checking_shopping_cart(demoshop):
    response = demoshop.post("/addproducttocart/catalog/31/1/1")
    assert response.status_code == 200


def test_update_shopping_cart(auth_user, demoshop):
    demoshop.post('/addproducttocart/catalog/31/1/1')
    auth_user.element('.ico-cart').click()
    auth_user.element('.qty-input').clear().send_keys(0).press_enter()
    auth_user.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_logout(demoshop):
    demoshop.get('logout')
