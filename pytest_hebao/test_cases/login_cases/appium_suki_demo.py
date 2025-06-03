import time
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as ec

desired_caps = {'appium:deviceName': '127.0.0.1：62025',
                'platformName': 'Android',
                'appium:automationName': 'uiautomator2',
                'appium:appPackage': 'com.masseffect.suki',
                'appium:appActivity': 'com.masseffect.suki.MainActivity',
                'appium:platformVersion': '9'}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

size = driver.get_window_size()
print(size)

wait = WebDriverWait(driver, 5, 0.5)
time.sleep(2)
# yszc_agree = wait.until(ec.presence_of_element_located((By.ID, '同意')))
# ys_agree = driver.find_element(MobileBy.ACCESSIBILITY_ID,('同意')
ys_agree = driver.find_element(MobileBy.ACCESSIBILITY_ID, "同意")
ys_agree.click()
# time.sleep(1)

wx_login = wait.until(ec.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, '微信登录')))
# wx_login = driver.find_element(MobileBy.ACCESSIBILITY_ID,('微信登录')
wx_login.click()
# time.sleep(2)

zc_agree = wait.until(ec.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'同意')))
# zc_agree = driver.find_element(MobileBy.ACCESSIBILITY_ID,'同意')
zc_agree.click()
time.sleep(1)

if driver.find_element(MobileBy.ACCESSIBILITY_ID,'去匹配'):
    driver.find_element(MobileBy.ACCESSIBILITY_ID,'去匹配').click()
    time.sleep(1)
    other_unm = input('请输入对方验证码：')
    driver.find_element(MobileBy.ACCESSIBILITY_ID,'点击输入对方验证码').send_keys(other_unm)
    time.sleep(1)
    ActionChains(driver).key_down('ENTER').perform()

# wd_butt = wait.until(ec.presence_of_element_located((By.ID, '问答')))
wd_butt = driver.find_element(MobileBy.ACCESSIBILITY_ID,'问答')
wd_butt.click()
time.sleep(1)
# if wait.until(ec.presence_of_element_located((By.ID, '领取新问答'))):
if driver.find_element(MobileBy.ACCESSIBILITY_ID,'领取新问答'):
    # wd_lq_butt = wait.until(ec.presence_of_element_located((By.ID, '领取新问答')))
    wd_lq_butt = driver.find_element(MobileBy.ACCESSIBILITY_ID,'领取新问答')
    wd_lq_butt.click()
    time.sleep(1)

    # driver.back()
    driver.keyevent(4)
    time.sleep(1)

elif driver.find_element(MobileBy.ACCESSIBILITY_ID,'双方回答完成后，开启新问答'):

    # driver.back()
    driver.keyevent(4)
    time.sleep(1)

xqrj_butt = driver.find_element(MobileBy.ACCESSIBILITY_ID,'心情日记')
xqrj_butt.click()
time.sleep(1)

# xrj_toast = wait.until(ec.presence_of_element_located((By.ID, '今天还没写日记')))
xrj_toast = driver.find_element(MobileBy.ACCESSIBILITY_ID,'今天还没写日记')
time.sleep(1)
if xrj_toast:
    driver.tap([(913, 2370)], 100)
    time.sleep(1)

else:

    try:
        for i in range(1, 31):
            driver.find_element_by_android_uiautomator(f'new UiSelector().description({i})').click()
            time.sleep(2)

            break
    except Exception as e:
        print(IndexError, e)
driver.find_element(MobileBy.ACCESSIBILITY_ID,'平静').click()
time.sleep(1)
rj_nr_input = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText')
rj_nr_input.send_keys('这是一句简单的介绍~~~~')
time.sleep(1)
driver.find_element(MobileBy.ACCESSIBILITY_ID,'添加').click()
time.sleep(1)
driver.tap([(600, 2400)], 100)
time.sleep(1)
try:
    driver.find_element(MobileBy.ACCESSIBILITY_ID,'允许使用').click()
    time.sleep(1)
    qx_butt = driver.find_elements(MobileBy.CLASS_NAME, 'android.widget.Button')
    qx_butt[0].click()
    time.sleep(1)
    driver.tap([(600, 2400)], 100)
except Exception as e:
    print(e, '不需要打开权限')
finally:
    time.sleep(10)
    driver.tap([(600, 2400)], 100)
    time.sleep(1)
    driver.find_element(MobileBy.ACCESSIBILITY_ID,'完成')

# driver.find_element(MobileBy.ACCESSIBILITY_ID,('完成').click()
driver.tap([(1057, 213)], 100)
time.sleep(1)
# driver.back()
driver.keyevent(4)
