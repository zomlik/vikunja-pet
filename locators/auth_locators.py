from selenium.webdriver.common.by import By


class AuthLocators:
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_ENTER = (By.XPATH, "//*[@data-v-fefdc249]")

    TEXT_HELLO_USER = (By.XPATH, "//h2[@data-v-746c9d2b]")
