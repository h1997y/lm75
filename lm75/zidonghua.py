from selenium import webdriver  # 从selenium工具中导入 webdriver 库
import time  # 导入time这个模块

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 选择chrome 浏览器，初始化driver   就可以跟浏览器进行沟通  建立绘画（session）
driver.implicitly_wait(10)    #隐式等待，默认等待5s
#   常规操作
driver.get("http://www.baidu.com")   # 打开一个网址
driver.maximize_window()   # 浏览器窗口最大化
time.sleep(3)  # 等待3s  默认 秒 为单位
driver.get("http://erp.lemfix.com")
# time.sleep (2)
# driver.back () #退回上一个页面
# #time .sleep (2)
# driver.forward() #前进道下一个页面
# #time .sleep(2)
# driver.refresh () # 刷新页面
# 5、退出
# driver.quit() #关闭驱动 sessionx 闭
# #driver.close() #关闭当前的窗口，不会退出会话

# 切换了页面，页面没加载完，元素不显示    加一个等待
# 三种等待方式
# 1.强制等待 time.sleep(3)
# 2.智能等待：
#     隐式等待：可以设置一个等待时间，等待时间未结束但元素已找到，则不等待，继续执行后面的代码
#       注： 一个session里只执行一次
#     显示等待 expected_condition == python班级
# 3.


# 非常规操作  元素定位
# 元素定位 常用： id name xpath  css class tag link partial_link 例： username = driver.find_element_by_id('username')
# 点击click  传值send_keys   获取页面文本text
driver.find_element(By.ID, "username").send_keys("test123")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "btnSubmit").click()

# xpath :
# 绝对路径：/html/body/div/div/div[1]/a/b  从根节点开始  有顺序性、继承关系    页面修改后容易失效，不稳定
# 1.!!相对路径!!：靠自己的特征定位
#  标签名+属性 = //标签名[@属性名=属性值]    例： //input[@id="username"]
# driver.find_element(By.XPATH, "//input[@id='username']").send_keys("test123")
# 2.层级定位  //标签名[@属性值]//标签名[@属性名=属性值]
page_title = driver.title   #获取页面标题
page_text = driver.find_element(By.XPATH, "//div[@class='login-logo']//b").text
# print(page_text)
if page_text == "柠檬ERP":
    print("这个页面标题是：{}".format(page_text))
else:
    print("这条测试不通过")
# time.sleep(3)
# 3.文本属性定位   //标签名[text()="文本内容"]     //b[text()="文本内容"]
# 4.包含属性值  //标签名[contains(@属性名/text(),属性值)]   //input[contains(@class,"username")]  //input[contains(text(),"文本")]

login_user = driver.find_element(By.XPATH, "//p[text() = '测试用户']").text
if login_user == "测试用户":
    print("这个登录用户是：{}".format(login_user))
else:
    print("这条测试不通过")
# 点击零售出库
driver.find_element(By.XPATH, "//span[text()='零售出库']").click()
time.sleep(2)
#点击搜索
#1. 识别是否有子页面的方式：页面层级路径里出现iframe，就需要去切换 iframe 才可以进行元素的定位
# 2.怎么切换
# 1） 找到这个iframe元素，切换
# id = driver.find_element(By.XPATH, "//iframe[@id='tabpanel-bafba10ab5-frame']")
# driver.switch_to.frame('tabpanel-bafba10ab5-frame')
# driver.find_element(By.ID, "searchNumber").send_keys("314")     定位不到元素
# 通过找到这个元素  获取id 属性 get_attribute()
P_id = driver.find_element(By.XPATH, "//div[text() = '零售出库']/..").get_attribute("id")
F_id = P_id+'-frame'
# 1.通过id进行的iframe切换
# driver.switch_to.frame(F_id)
# driver.find_element(By.ID, "searchNumber").send_keys("314")
# 2.通过元素定位（xpath）来切换iframe
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id = '{}']".format(F_id)))
# driver.find_element(By.ID, "searchNumber").send_keys("314")
# 3.iframe下标 从0开始 html页面-0，下一个为1 再下一个为2 找html
driver.switch_to.frame(1)
driver.find_element(By.ID, "searchNumber").send_keys("9247")
# 点击查询按钮
# 1）层级定位
# driver.find_element(By.XPATH, "//a[@id = 'searchBtn']//span").click()
# 2).文本属性定位   //标签名[text()="文本内容"]     //b[text()="文本内容"]
# driver.find_element(By.XPATH, "//span[text() = '查询']").click()
# 3)包含属性值定位  //标签名[contains(@属性名/text(),属性值)]
# driver.find_element(By.XPATH, "//span[contains(text(), '查询')]").click()
# 4).!!相对路径!!：靠自己的特征定位  例： //input[@id="username"]
driver.find_element(By.ID, "searchBtn").click()
time.sleep(3)
# 找到单据编号
num = driver.find_element(By.XPATH, "//tr[@id = 'datagrid-row-r1-2-0']//td[@field = 'number']/div").text
if "9247" in num:
    print("搜索结果正确")
else:
    print("测试不通过！")