from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
import datetime


def job():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/ul[1]/a[7]'))).click()
    time.sleep(5)
    if EC.alert_is_present():
        result = driver.switch_to.alert
        result.accept()
    else:
        print("alert error")
    print("current time: ", datetime.datetime.now(), " - clicked!")


service = Service('../chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('address')
time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div[1]/div/input'))).send_keys(
    "id")
driver.find_element("xpath", '//*[@id="login"]/div[2]/div/input').send_keys("password")
driver.find_element("xpath", '//*[@id="login"]/div[3]/div[2]/button').click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/center/table/tbody/tr[1]/td[2]/a'))).click()

##자동 로그아웃 됐을 경우 대비 필요
# schedule.every().hour.at(":00" or ":01" or ":05" or ":06").do(job)
schedule.every().day.at("09:00").do(job)
schedule.every().day.at("09:05").do(job)
schedule.every().day.at("10:00").do(job)
schedule.every().day.at("10:05").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("11:05").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("14:00").do(job)
schedule.every().day.at("14:05").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().day.at("15:05").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("16:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
