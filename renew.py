# renew.py 续费

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# 续费结算
checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '我已阅读，理解并确认以下协议内容')]")))
checkbox.click()

renew_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '去结算')]")))
renew_button.click()
