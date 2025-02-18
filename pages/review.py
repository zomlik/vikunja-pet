import allure

from locators.review_locators import ReviewLocators
from pages.base import BasePage


class Review(BasePage):
    def create_new_task(self, task_name: str) -> None:
        with allure.step(f"Ввести имя '{task_name}' для задачи"):
            self.find(ReviewLocators.NEW_TASK_FIELD).send_keys(task_name)
        with allure.step("Нажать на кнопку 'Добавить задачу'"):
            self.click(ReviewLocators.ADD_TASK_BUTTON)

    def list_of_tasks(self):
        return self.finds(ReviewLocators.LIST_OF_TASKS)
