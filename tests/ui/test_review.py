import allure

from pages.review import Review
from utils.url import URL


@allure.suite("Страница Обзор")
class TestReview:
    @allure.title("Создание новой задачи")
    def test_add_new_task(self, driver):
        name = "Задача"
        page = Review(driver)
        page.open(URL.MAIN_PAGE)
        page.create_new_task(name)
        assert page.list_of_tasks()[0].text == name
