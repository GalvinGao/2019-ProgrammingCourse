from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlencode
import requests
import random

CREDENTIALS = {
    "username": '8552571',
    "password": "FLZX3000chi"
}

driver = webdriver.Firefox()
driver.get("https://toefl.neea.cn/login")
time.sleep(5)
login_username_elem = driver.find_element_by_xpath('//*[@id="userName"]')
login_username_elem.clear()
login_username_elem.send_keys(CREDENTIALS['username'])
login_password_elem = driver.find_element_by_xpath('//*[@id="textPassword"]')
login_password_elem.clear()
login_password_elem.send_keys(CREDENTIALS['password'])
time.sleep(10)

def post():
    url = "https://pushbear.ftqq.com/sub?sendkey=4486-c645795fc87eba17e9313e7e1b46146b&text={TITLE}&desp={DESC}"
    formatted = url.format(TITLE=urlencode('托福成绩疑似出现！'),
                           DESC=urlencode('托福成绩疑似出现！快到 https://toefl.neea.cn/ 使用大师球捕获！'))
    requests.get(formatted)

def check():
    driver.refresh()
    time.sleep(5)
    check_grade_btn = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/ul/li[14]/a')
    check_grade_btn.click()
    time.sleep(3)
    try:
        assert "0000000032928839" in driver.page_source
    except AssertionError:
        time.sleep(10)
    latest_grade_elem = driver.find_element_by_xpath('//*[@id="wg_center"]/div/div[3]/div/table[1]')
    latest_grade_elem.find_element_by_xpath('//*[@id="wg_center"]/div/div[3]/div/table[1]/tbody/tr[6]/td[1]')
    if latest_grade_elem.text == "成绩":
        print("成 绩 觉 察 ！ 正在通知...")
        post()
    else:
        ran = random.randint(600, 1800)
        print("还没出分... 将在 {SEC} 秒后重新检查...".format(SEC=ran))
        time.sleep(ran)
        check()

check()
driver.close()
