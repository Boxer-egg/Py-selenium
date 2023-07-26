

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def setup_browser():
    driver = webdriver.Firefox()
    driver.get(config['AgentLoginLink'])
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys(config['username'])
    password.send_keys(config['password'])
    password.send_keys(Keys.RETURN)
    return driver


def test_step_11(driver):
    # 执行第11步的代码
    pass


def test_step_12(driver):
    # 执行第12步的代码
    pass


def test_step_14(driver):
    # 执行第14步的代码
    pass


driver = setup_browser()
test_step_11(driver)
test_step_12(driver)
test_step_14(driver)
