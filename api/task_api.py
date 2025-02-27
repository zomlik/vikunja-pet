from typing import Type

import allure
from pydantic import BaseModel, ValidationError

from api.api_client import ApiClient
from models.task_model import CreateTask
from utils.url import Endpoints


class TaskApi(ApiClient):
    @allure.step("Создать новую задачу")
    def create_task(self, json: CreateTask, id_project: int):
        return self.put(url=f"{Endpoints.BASE}/projects/{id_project}/tasks",
                        playload=json.model_dump())

    def get_all_tasks(self):
        return self.get(url=Endpoints.GET_ALL_TASKS)

    @allure.step("Валидация JSON схемы")
    def check_json_schema(self, model: Type[BaseModel]):
        try:
            data = self.get_json()
            validate_data = model(**data)
            return validate_data
        except ValidationError as e:
            raise e
