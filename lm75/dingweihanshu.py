import time  # 导入time这个模块

from selenium.webdriver.common.by import By

def login_page(username,password,driver):   # 形参  参数化  提高代码复用率
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "btnSubmit").click()
def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()
def search_key(url, driver, username, password, s_key):
    open_url(url, driver)
    login_page(username, password, driver)
    driver.find_element(By.XPATH, "//span[text()='零售出库']").click()
    P_id = driver.find_element(By.XPATH, "//div[text() = '零售出库']/..").get_attribute("id")
    F_id = P_id+'-frame'
    driver.switch_to.frame(1)
    driver.find_element(By.ID, "searchNumber").send_keys(s_key)
    driver.find_element(By.ID, "searchBtn").click()
    time.sleep(3)
    num = driver.find_element(By.XPATH, "//tr[@id = 'datagrid-row-r1-2-0']//td[@field = 'number']/div").text
    return num