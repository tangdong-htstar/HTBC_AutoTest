from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchDriverException
import time
from config import VM

driver = webdriver.Chrome()
url = "http://172.18.11.231:8081/#/login"
driver.get(url)
driver.maximize_window()
sendname = driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[1]/div/input').send_keys(VM.name)
sendpsd = driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[2]/div/input').send_keys(VM.passport)
sendVF = driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[3]/div[1]/input').send_keys(VM.PC_verification_code)
sendVF = driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/button').click()

time.sleep(5)
# alert=driver.switch_to.alert
# alert.accept()
# view_now_botton = driver.find_element(By.XPATH,'//*[@id="home"]/div[5]/div/div[3]/div/button[2]/span').click()
boton_text=driver.find_element(By.XPATH,value='//*[@id="home"]/div[5]/div/div[3]/div/button[2]/span').text
print(boton_text)
assert boton_text == '立即查看'
time.sleep(10)
# # while True:
#     pass