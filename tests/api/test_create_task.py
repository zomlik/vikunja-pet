import allure

from api.task_api import TaskApi
from data.create_new_task import Task


@allure.suite("Задачи")
class TestTasks:
    @allure.title("Создать задачу с значением из 1 символа")
    def test_create_new_task(self):
        r = TaskApi()
        r.create_task(id=9, json=Task.Task_1)
