import os


class URL:
    MAIN_PAGE = os.getenv("BASE_URL")


class Endpoints:
    BASE = os.getenv("BASE_API")
    LOGIN = f"{BASE}/login"
    REGISTER = f"{BASE}/register"
