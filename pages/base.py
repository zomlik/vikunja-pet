import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, timeout=10)

    @allure.step("Открытие страницы")
    def open(self, url: str) -> None:
        return self.driver.get(url)

    @allure.step("Поиск элемента на странице")
    def find(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Поиск всех элементов на странице")
    def finds(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Клик по элементу")
    def click(self, locator: tuple[str, str]) -> None:
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получение текста")
    def get_text(self, locator: tuple[str, str]) -> str:
        return self.find(locator).text
