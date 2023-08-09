from lm75 import dingweihanshu
from test_data import test_date
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)    #隐式等待，默认等待5s
# 调用函数   取参  传参到函数调用里
url = test_date.url["url"]
user = test_date.login_date["username"]
pwd = test_date.login_date["password"]
s_key = test_date.s_key["s_key"]

# 函数调用 传参   给函数定义一个返回值  调用的时候用一个变量接受返回值
result = dingweihanshu.search_key(driver=driver, url=url, username=user, password=pwd, s_key=s_key)

if s_key in result:
    print("搜索结果正确")
else:
    print("测试不通过！")

