# renew.py 续费

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def renew_function(driver, real_product_name):
    # 使用 real_product_name 在此处查找并点击续费按钮
    renew_button_xpath = f"//a[contains(@href, \"{real_product_name}\") and contains(@class, 'btn')]"
    renew_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, renew_button_xpath)))
    renew_button.click()

    # 提交结算
    renew_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_lockated((By.XPATH, "//button[contains(text(), '去结算')]")))
    renew_button.click()

    renew_checkbox = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '我已阅读，理解并确认以下协议内容')]")))
    renew_checkbox.click()

    confirm_payment_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//button/span[text()="提交订单"]')))
