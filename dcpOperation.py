

import time
from selenium import webdriver

driver = webdriver.Firefox()


with open('config.yaml') as f:
    config = yamal.safe_load(f)

driver.get('dcp连接')
time.sleep(1)
