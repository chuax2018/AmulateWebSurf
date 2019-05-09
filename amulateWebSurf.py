from selenium import webdriver
import os
import time

# 构造模拟浏览器
chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
time.sleep(2)
url = "https://www.baidu.com/"
driver.get(url)  # 打开网址
# driver.maximize_window() #窗口最大化

# 模拟登陆
time.sleep(2)
# driver.find_element_by_name('tj_login').click() #这样写报错：元素不可见，所以用万能的Xpath
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()  # 点击登录按钮
time.sleep(2)
driver.find_element_by_name('userName').clear()  # 先清除输入框内容
driver.find_element_by_name('userName').send_keys(u'000000')  # 输入账号
time.sleep(1)
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys(u'000000')  # 输入密码