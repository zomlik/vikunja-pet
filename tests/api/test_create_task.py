import allure

from api.task_api import TaskApi
from models.task_model import CreateTask


@allure.suite("Задачи")
class TestTasks:
    @allure.title("Создать задачу с значением из 1 символа")
    def test_create_new_task(self, get_token, get_project_id):
        r = TaskApi(get_token)
        r.create_task(json=CreateTask(
            title="Для меня",
            project_id=get_project_id
        ), id_project=get_project_id)
        assert r.check_json_schema(CreateTask)
        assert r.status_code() == 201
