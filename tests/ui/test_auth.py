import os

import allure

from pages.auth import Auth
from utils.url import URL


@allure.title("Авторизация пользователя")
def test_auth(driver):
    page = Auth(driver)
    page.open(URL.MAIN_PAGE)
    page.do_auth(login=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))
    with allure.step("Пользователь успешно авторизован"):
        assert os.getenv("LOGIN") in page.text_hello_user()
