from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

# 初始化 WebDriver

driver = webdriver.Chrome()

# 访问网站
driver.get("https://petstore.octoperf.com/actions/Catalog.action")

# 最大化窗口（可选）
driver.maximize_window()

# 点击登录按钮
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
)
login_button.click()

# 输入用户名和密码
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
actions = ActionChains(driver)
actions.move_to_element(username_field).click().send_keys("j2ee").perform()

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_field.clear()
actions = ActionChains(driver)
actions.move_to_element(password_field).click().send_keys("j2ee").perform()

# 增加等待提交按钮
login_submit = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "signon"))
)
login_submit.click()

# 验证是否成功登录（依据你的网站改变内容）
try:
    assert "My Account" in driver.page_source
    print("Login was successful")
except AssertionError:
    print("Login failed")
    
time.sleep(10)

# 关闭浏览器
driver.quit()
