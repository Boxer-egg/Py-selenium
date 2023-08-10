import time
import yaml
import logAndjump  # 登录和跳转函数
from logAndjump import print_time
# import renew  # 续费函数
from reportDoc import Report
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


# 创建一个新的浏览器实例
driver = webdriver.Firefox()
print('创建成功')

# 打开配置文件
with open('config.yaml') as f:
    config = yaml.safe_load(f)


# 登录
driver.get(config['AgentLoginLink'])
time.sleep(0.5)
logAndjump.RunLogin(driver, config['username1'], config['password1'])

# Report.add_line('登录成功，页面为：' + config['AgentLoginLink'])

# 跳转到购买链接

time.sleep(1)


driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
# logAndjump.HomePage(driver)
driver.get(config['HomePage'])

# 搜索商品名
time.sleep(0.5)
current_time = time.strftime("%m%d-%H%M")
product_name = f"test{current_time}xn"
Suffix = ".com"  # 这里配置后缀
real_product_name = product_name + Suffix

search_box = driver.find_element(By.ID, "prefix")
search_box.send_keys(real_product_name)  # 使用real_product_name变量
print('搜索产品成功：', real_product_name, print_time())
# Report.add_line('搜索产品成功：' + real_product_name)

# 点击搜索
query_button = driver.find_element(By.ID, "queryDomain")
query_button.click()
print('搜索按钮点击成功', print_time())

# 加入清单
add_to_list_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, f'//a[@data-domain="__{real_product_name}__"]')))  # 使用real_product_name变量
add_to_list_button.click()
print('已加入购物车', print_time())

time.sleep(1)

# 点击域名清单
domain_list = driver.find_element(By.ID, "badge-num")
domain_list.click()
print('点击清单成功', print_time())

time.sleep(1)
# 确认清单已经加入购买的商品
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
    (By.XPATH, '//td[@class="col1"]/div'), real_product_name))  # 使用real_product_name变量


# 点击立即结算
time.sleep(0.5)
checkout_button = driver.find_element(By.ID, "toPayment")
checkout_button.click()

# 等待链接跳转 或者页面元素有更新
time.sleep(0.5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, config['ReadyToPay'])))
print("结算页面，加载成功", print_time())
# 单选模板
time.sleep(1)
template = driver.find_element(By.XPATH, config['TemplateName'])
template.click()
print('勾选模板成功', print_time())


# 勾选同意协议
# 找到一个特定的复选框，确保它在视图中，然后点击它
checkbox = driver.find_element(By.CSS_SELECTOR, config['Agreement'])
# By.CSS_SELECTOR作为查找方法
checkbox.location_once_scrolled_into_view
# 确保元素（复选框）滚动到视图中。如果元素在当前视图之外（在页面底部，而页面没有完全滚动到底部），
# 会自动滚动页面，使元素可见。
actions = ActionChains(driver)
# 创建了一个新的ActionChains对象。
# ActionChains是Selenium提供的一个工具，允许你串联多个动作（如点击、拖放等）并一次性执行它们。
actions.move_to_element(checkbox).click(checkbox).perform()
print('协议已勾选', print_time())


# 点击“提交订单”按钮
submit_order_button = driver.find_element(
    By.XPATH, '//button/span[text()="提交订单"]')
submit_order_button.click()
print("提交按钮点击成功", print_time())


# 等待链接变化 或出现“确认支付”按钮
confirm_payment_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//button/span[text()="确认支付"]')))
print('获取按钮：“确认支付”', print_time())

confirm_payment_button.click()

print('支付成功', print_time())

# 打开管理列表，查看产品
driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get(config['ManageList'])

time.sleep(2)
# 时间倒序排列
sort_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//em[@data-id="apply_date:desc"]')))
sort_button.click()

#renew.renew_function(driver, real_product_name)

# 调用续费函数


'''
你可以使用Python的`assert`语句来测试你的代码。`assert`语句用于断言某个条件是真的，
如果条件为假，那么程序会抛出一个`AssertionError`异常。

例如，你可以在点击“确认支付”按钮之后，检查按钮是否仍然存在。
如果按钮仍然存在，那么说明点击操作可能没有成功。你可以这样写：

```python
confirm_payment_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//button/span[text()="确认支付"]')))
confirm_payment_button.click()

# 检查按钮是否仍然存在
try:
    driver.find_element(By.XPATH, '//button/span[text()="确认支付"]')
    print("确认支付按钮仍然存在，点击操作可能没有成功。")
except NoSuchElementException:
    print("确认支付按钮已经消失，点击操作成功。")
```

对于勾选同意协议的部分，你可以在勾选之后，检查复选框的状态是否为已勾选：

```python
agree_checkbox = driver.find_element(By.XPATH, config['Agreement'])
agree_checkbox.click()

# 检查复选框是否已勾选
assert agree_checkbox.is_selected(), "复选框没有被勾选。"



这段代码会检查`agree_checkbox`是否已被勾选。
如果没有被勾选，那么`assert`语句会抛出一个`AssertionError`异常。

这样，你就可以通过观察程序的输出或者是否抛出异常
来判断你的代码是否按照预期工作。

'''
