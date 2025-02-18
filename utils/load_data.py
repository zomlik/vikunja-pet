import os

import requests

from utils.url import Endpoints


def load_data():
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    email = os.getenv("EMAIL")

    try:
        r = requests.post(
            url=Endpoints.LOGIN,
            data={
                "username": login,
                "password": password
            })
        if r.status_code == 412:
            r = requests.post(
                url=Endpoints.REGISTER,
                data={
                    "email": email,
                    "username": login,
                    "password": password
                })
            assert r.status_code == 200, (f"Ожидаемый статус код: 200,"
                                          f" Фактический {r.status_code}")
    except Exception as e:
        raise e
