from ast import Bytes

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="session")
def driver():
    desired_caps ={
        "platformName":"Android",
        "devicesName":"127.0.0.1:62025",
        "platformVersion":"9",
        "appPackage":"com.ppmm.hebao",
        "appActivity":"com.ppmm.hebao.MainActivity",
        "automationName":"UIAutomator2"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    yield driver
    size = driver.get_window_size()
    yield size
    wait = WebDriverWait(driver,5,0.5)
    driver.quit()


def login(driver):
    driver.find_element(By.CLASS_NAME,'android.view.View').click()
    driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="手机号登录"]').click()
    driver.find_element(By.CLASS_NAME,'android.widget.EditText').send_keys('19987434952')
    driver.find_element(By.accessibility_id,"下一步").click()
    driver.find_element(By.ACCESSIBILITY_ID, 'your_accessibility_id')


if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])

