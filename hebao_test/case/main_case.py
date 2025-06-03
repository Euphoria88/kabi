# coding=utf-8
import time
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as ec

desired_caps = {'appium:deviceName': '127.0.0.1:62025',
                'platformName': 'Android',
                'appium:automationName': 'UiAutomator2',  # 必须
                'appium:appPackage': 'com.ppmm.hebao',
                'appium:appActivity': 'com.ppmm.hebao.MainActivity',
                'appium:platformVersion': '9'}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 点击“同意”按钮
driver.find_element(MobileBy.ACCESSIBILITY_ID, '同意').click()
# 点击“隐私政策同意选中框”按钮
driver.find_element(MobileBy.CLASS_NAME,'android.widget.ImageView').click()
# 点击“手机号登录”按钮
driver.find_element(MobileBy.ACCESSIBILITY_ID, '手机号登录').click()
# 输入手机号
driver.find_element(MobileBy.ACCESSIBILITY_ID,'请输入手机号').send_keys('19987434952')
# 点击“下一步”按钮
driver.find_element(MobileBy.ACCESSIBILITY_ID, '下一步').click()
# 用于生成xpath定位 获取toast提示框文本信息
toast_message = '^\d{n}$'
message ='//*[@text=\'{}\']'.format(toast_message)

# 获取toast提示框内容
toast_element = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)
assert toast_element.text == toast_message
# 输入验证码
driver.find_element(MobileBy.ACCESSIBILITY_ID, '请输入验证码').send_keys('')


