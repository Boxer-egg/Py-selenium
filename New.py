import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options


# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)

# 创建一个新的浏览器实例
driver = webdriver.Firefox()


try:
    with open('config.yaml') as f:
        config = yaml.safe_load(f)

except FileNotFoundError:
    print("没有找到配置文件 'config.yaml'。")
except KeyError as e:
    print(f"配置文件 'config.yaml' 中缺少必要的字段：{e}")


# 登录
driver.get(config['AgentLoginLink'])
time.sleep(0.5)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys(config['username'])
password.send_keys(config['password'])
password.send_keys(Keys.RETURN)  # 摁下回车

time.sleep(3)
# 等待URL变化
# WebDriverWait(driver, 12).until(EC.url_changes(driver.current_url))
# 等待头像加载出现
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'img[src="/agent/static/img/home/img_01.png"]')))

# 选择InternalInfo文件内的CreateTemplateAddress命名的链接，内新建模板
driver.get(config['CreateTemplateAddress'])

time.sleep(2)
# 填写模板名称
template_type = driver.find_element(By.ID, "templateName")
template_type.send_keys("模板测试" + time.strftime("%m-%d｜%I:%M:%S｜%p"))

# 选择用户类型
user_type = driver.find_element(
    By.CSS_SELECTOR, 'input[name="typeRadio"][value="P"]')  # 选择个人
user_type.click()

# 选择证件类型
# 点击 <label> 元素以打开下拉列表
driver.find_element(By.ID, "idTypeLabel").click()

# 从 <ul> 元素中找到 "身份证" 的 <li> 元素，并点击它
driver.find_element(By.XPATH, '//li[text()="身份证"]').click()
'''
这个代码首先点击 ID 为 "idTypeLabel" 的 <label> 元素以打开下拉列表，
然后从 <ul> 元素中找到文本为 "身份证" 的 <li> 元素，并点击它，从而选择 "身份证" 这个选项。

请注意，这个代码可能需要根据你的实际网页进行调整。
如果你的网页有多个 <li> 元素的文本都是 "身份证"，
你可能需要提供更具体的 XPath 表达式来定位正确的 <li> 元素。
'''
# 上传文件  ta
file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
file_input.send_keys("/Users/box/Desktop/个人证件/sfz2.jpg")
time.sleep(2)

# 填写域名联系人
contact_person = driver.find_element(By.ID, "userNameCn")
contact_person.send_keys(config['contact_person'])

time.sleep(0.5)
driver.execute_script("window.scrollBy(0, 200);")


# 找到输入框元素organCode
input_element_organCode = driver.find_element(By.ID, "organCode")
# 获取输入框的值
input_value = input_element_organCode.get_attribute("value")
# 判断输入框的值是否为空
if input_value:
    # 输入框有值，略过
    print("输入框已有值:", input_value)
else:
    # 输入框没有值，录入预设的值
    preset_value = config['ID']
    input_element_organCode.send_keys(preset_value)
    print("录入预设的值:", preset_value)


# 找到输入框元素organizeNameCn
input_element_organizeNameCn = driver.find_element(By.ID, "organizeNameCn")
# 获取输入框的值
input_value = input_element_organizeNameCn.get_attribute("value")
# 判断输入框的值是否为空
if input_value:
    # 输入框有值，略过
    print("输入框已有值:", input_value)
else:
    # 输入框没有值，录入预设的值
    preset_value = "新网测试"
    input_element_organizeNameCn.send_keys(preset_value)
    print("录入预设的值:", preset_value)
time.sleep(0.5)

# 找到输入框元素publicStreetCn
input_element_publicStreetCn = driver.find_element(By.ID, "publicStreetCn")
# 获取输入框的值
input_value = input_element_publicStreetCn.get_attribute("value")
# 判断输入框的值是否为空
if input_value:
    # 输入框有值，略过
    print("输入框已有值:", input_value)
else:
    # 输入框没有值，录入预设的值
    preset_value = "地球村北京市"
    input_element_publicStreetCn.send_keys(preset_value)
    print("录入预设的值:", preset_value)


# 选择所属区域
# 点击 "请选择" label 打开国家选择下拉列表
driver.find_element(By.XPATH, '//label[text()="请选择"]').click()

# 从下拉列表中选择 "中国"
driver.find_element(By.XPATH, '//li[text()="中国"]').click()

# 等待一下，让页面有时间更新
time.sleep(1)

# 点击 "请选择" label 打开省份选择下拉列表
driver.find_element(By.ID, "provinceLable").click()

# 从下拉列表中选择 "北京市"
driver.find_element(By.XPATH, '//li[text()="北京市"]').click()

# 等待一下，让页面有时间更新
time.sleep(1)


# 点击 "请选择" label 打开城市选择下拉列表
driver.find_element(By.ID, "cityLable").click()

# 找到 "北京市" 的 <li> 元素并点击
# driver.find_element(By.XPATH, '//li[text()="北京市"]').click()
#<li onclick="setCity('110100')" selectid="110100" class="selected">北京市</li>
driver.find_element(By.XPATH, '//li[@selectid="110100"]').click()
driver.execute_script("window.scrollBy(0, 100);")


# 填写邮政编码
postal_code = driver.find_element(By.ID, "publicZipCode")
postal_code.send_keys("100710")

# 填写电子邮箱
email = driver.find_element(By.ID, "userEmail")
email.send_keys(config['Email'])

# 填写电话
# phone1 = driver.find_element(By.ID, "userPhoneInter")
# phone1.send_keys("86")
phone2 = driver.find_element(By.ID, "userPhoneArea")
phone2.send_keys(config['phone2'])
phone3 = driver.find_element(By.ID, "userPhoneNumber")
phone3.send_keys(config['phone3'])

# 填写传真
# Fax1 = driver.find_element(By.ID, "userFaxInter")
# Fax1.send_keys("86")
Fax2 = driver.find_element(By.ID, "userFaxArea")
Fax2.send_keys(config['Fax2'])
Fax3 = driver.find_element(By.ID, "userFaxNumber")
Fax3.send_keys(config['Fax3'])
time.sleep(0.5)

# 填写域名所有人（英文）
domain_owner = driver.find_element(By.ID, "organizeNameUk")
domain_owner.send_keys("NCS")
driver.execute_script("window.scrollBy(0, 120);")


# 填写域名联系人（英文）
contact_person_en1 = driver.find_element(By.ID, "userSurnameUk")
contact_person_en1.send_keys("xin")
contact_person_en2 = driver.find_element(By.ID, "userNameUk")
contact_person_en2.send_keys("Net")

# 填写通信地址（英文）
address_en = driver.find_element(By.ID, "publicStreetUk")
address_en.send_keys("beijingshi")
time.sleep(0.5)

# 点击提交按钮
submit_button = driver.find_element(By.ID, "submitButtonId")
submit_button.click()


# 检查弹窗
try:
    # 找到弹窗元素
    popup = driver.find_element(By.ID, "popup")

    # 找到弹窗的内容元素
    popup_body = popup.find_element(By.ID, "popBody")

    # 打印弹窗的内容
    print(popup_body.text)
except NoSuchElementException:
    print("没有找到录入异常弹窗")


try:
    # 找到弹窗元素
    popup = driver.find_element(By.ID, "confirm1690047098636")

    # 检查弹窗的标题和内容
    if "操作提示" in popup.text and "您的信息填写不完整或不规范，请核实修改后提交！" in popup.text:
        # 找到并点击"确认"按钮
        confirm_button = popup.find_element(By.CSS_SELECTOR, ".btnYes")
        confirm_button.click()

except NoSuchElementException:
    print("模板创建成功")
    # 点击提交按钮
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".xwDialogConfirm")))
    submit_button.click()


# 关闭浏览器
# driver.quit()
