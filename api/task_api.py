import allure
from api.api_client import ApiClient
from models.task_model import CreateTask
from utils.url import Endpoints


class TaskApi(ApiClient):
    @allure.step("Создать новую задачу")
    def create_task(self, json: CreateTask, id_task: int):
        return self.put(url=f"{Endpoints.BASE}/{id_task}/tasks",
                        json=json.model_dump())
