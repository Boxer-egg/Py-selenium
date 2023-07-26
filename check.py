
import InternalInfo


# 在链接B内查询模板
driver.get("链接B")
search_box = driver.find_element_by_name("search_box")  # 请替换为实际的搜索框的name属性
search_box.send_keys("模板名称")  # 请替换为实际的模板名称
search_box.send_keys(Keys.RETURN)

# 点击详情并查看
detail_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "detail_button"))  # 请替换为实际的详情按钮的name属性
)
detail_button.click()

# 检查录入的N条数据
# 这里需要添加检查数据的代码
