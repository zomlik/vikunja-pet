import requests

from utils.logger import log


class ApiClient:
    def __init__(self):
        self.response = None
        self.token = None
        self.timeout = 10

    def get(self, url: str, query: dict = None):
        self.response = requests.get(url=url,
                                     headers={
                                         "Authorization": f"Bearer {self.token}"
                                     },
                                     params=query,
                                     timeout=self.timeout)

    def post(self, url: str, data: dict = None):
        self.response = requests.post(url=url,
                                      json=data,
                                      headers={
                                          "Authorization": f"Bearer {self.token}"
                                      },
                                      timeout=self.timeout)
        log(self.response, json=data)

    def put(self, url: str, playload: dict = None):
        self.response = requests.put(url=url,
                                     json=playload,
                                     headers={
                                         "Authorization": f"Bearer {self.token}"
                                     },
                                     timeout=self.timeout)
        log(self.response, json=playload)

    def delete(self, url: str):
        pass

    def get_json(self):
        return self.response.json()
