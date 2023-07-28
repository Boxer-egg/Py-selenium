import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver


with open('config.yaml') as f:
 # 安全模式打开
    config = yaml.safe_load(f)


def RunAgnetLogin(dirver, config):
    '''
    执行代理登录操作
    放到括号内，函数可以接受这两个参数，并在函数体内执行。
    将 driver 和 config 的值传递给 RunAgnetLogin 函数。
    然后，RunAgnetLogin 函数可以使用这些值来执行登录操作。
    '''
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys(config['username'])
    password.send_keys(config['password'])
    password.send_keys(Keys.RETURN)
    print('执行成功时间', time)


def RunHyLogin(dirver, config):
    '''
    执行会员登录操作
    '''
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys(config['username'])
    password.send_keys(config['password'])
    password.send_keys(Keys.RETURN)
    print('登录成功时间', time)


def jumpAgentLogin(dirver):
    driver.get(config['AgentLoginLink'])


def jumpHylogin(dirver):
    """
    跳转到普通用户登录
    """
    pass


def jumpDCP(dirver):

'''
 跳到dcp
'''
    pass


def jumpHomePage(dirver):
    driver.get(config['HomePage'])


'''
跳到首页
'''
    pass


def jumpBosslogin(dirver):


'''
跳到boss登录
'''
    pass


def jumpRefund(dirver):


'''
跳到退费
'''
    pass


def 2():
    pass
