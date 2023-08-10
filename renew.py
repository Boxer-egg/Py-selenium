# renew.py 续费

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver


# 创建一个新的浏览器实例
driver = webdriver.Firefox()
print('创建成功')

# 登录
driver.get(config['AgentLoginLink'])
time.sleep(0.5)
logAndjump.RunLogin(driver, config['username1'], config['password1'])
print('登录成功，使用账户：', config['username1'])
# 跳转到tab2
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get(config['ManageList'])
print('跳转到产品管理页面')


def renew_function(driver, real_product_name):
    # 使用 real_product_name 在此处查找并点击续费按钮
    renew_button_xpath = f"//a[contains(@href, \"{real_product_name}\") and contains(@class, 'btn')]"
    renew_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, renew_button_xpath)))
    renew_button.click()
    print("点击续费按钮成功")

    # 提交结算
    renew_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_lockated((By.XPATH, "//button[contains(text(), '去结算')]")))
    renew_button.click()

    renew_checkbox = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '我已阅读，理解并确认以下协议内容')]")))
    renew_checkbox.click()
    print("勾选协议")

    confirm_payment_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//button/span[text()="提交订单"]')))
    print("提交订单")
