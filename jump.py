
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import yaml
import renew  # 续费函数


# 打开配置文件
with open('config.yaml') as f:
    config = yaml.safe_load(f)

driver = webdriver.Firefox()


def setup_browser():
    '''
    会设置浏览器到一个特定的状态（登录到网站）。
    '''
    driver = webdriver.Firefox()
    driver.get(config['AgentLoginLink'])
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys(config['username1'])
    password.send_keys(config['password1'])
    password.send_keys(Keys.RETURN)
    return driver


def test_step_11(driver):
    renew.renew_function(driver, real_product_name)


driver = setup_browser()
test_step_11(driver)
