from api.api_client import ApiClient
from utils.url import Endpoints


class ProjectAPI(ApiClient):
    def get_project(self):
        return self.get(Endpoints.GET_ALL_PROJECTS)

    def get_projects_ids(self):
        return self.get_json()[0]["id"]
