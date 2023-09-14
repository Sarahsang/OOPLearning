from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化WebDriver
driver = webdriver.Chrome()

try:
    # 打开Google网站
    driver.get("https://www.google.com")
    
    # 放大窗口
    driver.maximize_window()

    # 定位搜索框并输入“Hello World”
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Hello World")

    # 按回车键进行搜索
    search_box.send_keys(Keys.RETURN)
    
    # 等待搜索结果页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    
except Exception as e:
    print(f"An error occurred: {e}")
    
input("Press Enter to close...")