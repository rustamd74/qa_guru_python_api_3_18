import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from utils.base_session import BaseSession

browser.config.base_url = "https://demowebshop.tricentis.com"

load_dotenv()


@pytest.fixture(scope="session")
def demoshop():
    api_url = BaseSession(os.getenv("API_URL"))
    return api_url


@pytest.fixture(scope="session")
def auth_user(demoshop):
    response = demoshop.post("/login", json={"Email": os.getenv('LOGIN'), "Password": os.getenv('PASSWORD')},
                             allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    response.status_code == 302

    browser.open("")

    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': authorization_cookie})
    return browser


@pytest.fixture(scope="session")
def regres_api():
    return BaseSession(os.getenv('REG_URL'))
