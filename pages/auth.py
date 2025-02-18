import allure

from locators.auth_locators import AuthLocators
from pages.base import BasePage


class Auth(BasePage):
    @allure.step("Выполнение авторизации")
    def do_auth(self, login: str, password: str) -> None:
        self.find(AuthLocators.USERNAME).send_keys(login)
        self.find(AuthLocators.PASSWORD).send_keys(password)
        self.click(AuthLocators.BUTTON_ENTER)

    @allure.step("Получение текста приветствия")
    def text_hello_user(self) -> str:
        return self.get_text(AuthLocators.TEXT_HELLO_USER)
