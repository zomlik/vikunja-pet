import os

import requests

from utils.logger import log
from utils.url import Endpoints


def load_data():
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    email = os.getenv("EMAIL")

    login_data = {
        "username": login,
        "password": password
    }

    register_data = {
        "email": email,
        "username": login,
        "password": password
    }

    try:
        r = requests.post(
            url=Endpoints.LOGIN,
            json=login_data)
        log(response=r, json=login_data)

        if r.status_code == 412:
            r = requests.post(
                url=Endpoints.REGISTER,
                json=register_data)
            assert r.status_code == 200, (f"Ожидаемый статус код: 200,"
                                          f" Фактический {r.status_code}")
            log(response=r, json=register_data)
    except Exception as e:
        raise e
