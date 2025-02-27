import logging
import os
from datetime import datetime

import allure
import pytest
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.project_api import ProjectAPI
from pages.auth import Auth
from utils.load_data import load_data
from utils.url import URL, Endpoints


LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    load_dotenv()
    load_data()


def pytest_addoption(parser):
    parser.addoption("--ci", action="store_true", help="Запустить браузер в headless режиме")


@pytest.fixture()
def chrome_options(request):
    options = Options()
    if request.config.getoption("ci"):
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    return options


@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()


@pytest.fixture()
def get_token():
    r = requests.post(Endpoints.LOGIN, json={
        "username": LOGIN,
        "password": PASSWORD
    })
    return r.json()["token"]


@pytest.fixture()
def get_project_id(get_token):
    r = ProjectAPI(get_token)
    r.get_project()
    return r.get_projects_ids()


@pytest.fixture(autouse=True)
def auth(driver):
    try:
        page = Auth(driver)
        page.open(URL.MAIN_PAGE)
        page.do_auth(login=LOGIN, password=PASSWORD)
        assert LOGIN in page.text_hello_user()
    except Exception as e:
        raise e


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    try:
        if rep.when == "call" and rep.failed:
            browser = item.funcargs["driver"]
            allure.attach(browser.get_screenshot_as_png(),
                          name=f"Screenshot {datetime.now()}",
                          attachment_type=allure.attachment_type.PNG)
    except KeyError:
        pass
    except Exception as e:
        raise e
