from selenium.webdriver.common.by import By


class ReviewLocators:
    NEW_TASK_FIELD = (By.XPATH, "//textarea")
    ADD_TASK_BUTTON = (By.XPATH, "//button[@data-v-fefdc249]")

    LIST_OF_TASKS = (By.CSS_SELECTOR, ".task-link")
