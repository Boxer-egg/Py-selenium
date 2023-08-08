import time
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


with open('config.yaml') as f:
 # 安全模式打开
    config = yaml.safe_load(f)


def RunLogin(driver, username, password):
    '''
    执行代理登录操作
    放到括号内，函数可以接受这两个参数，并在函数体内执行。
    将 driver 和 config 的值传递给 RunAgnetLogin 函数。
    然后，RunAgnetLogin 函数可以使用这些值来执行登录操作。
    '''
    username_element = driver.find_element(By.NAME, "username")
    password_element = driver.find_element(By.NAME, "password")
    username_element.send_keys(username)
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)
    print('登录成功时间', time.ctime())


def jump_to_page(driver, config_key):
    """
    根据配置键跳转到相应的页面
    """
    driver.get(config[config_key])
