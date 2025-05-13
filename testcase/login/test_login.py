import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from config import VM

class Test_LoginError:

    # def test_loginZuDiE_001(self):
    #     print('\n运营账户登录租的易成功')
    #     driver = webdriver.Chrome()
    #     url = "http://172.18.11.231:8081/#/login"
    #     driver.get(url)
    #     driver.maximize_window()
    #     driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[1]/div/input').send_keys(
    #         VM.name)
    #     driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[2]/div/input').send_keys(
    #         VM.passport)
    #     driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[3]/div[1]/input').send_keys(
    #         VM.PC_verification_code)
    #     driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/button').click()
    #     time.sleep(5)
    #     boton_text = driver.find_element(By.XPATH, value='//*[@id="home"]/div[5]/div/div[3]/div/button[2]/span').text
    #     print(boton_text)
    #     assert boton_text == '立即查看'
    #     time.sleep(10)

    def test_loginZuDiE_002(self):
        print('\n运营账户登录租的易-不输入账号')
        driver = webdriver.Chrome()
        url = "http://172.18.11.231:8081/#/login"
        driver.get(url)
        driver.maximize_window()
        driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[1]/div/input').clear()
        driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[2]/div/input').send_keys(
            VM.passport)
        driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/div[3]/div[1]/input').send_keys(
            VM.PC_verification_code)
        driver.find_element(By.XPATH,value='//*[@id="login"]/div[1]/div[2]/div/div[2]/button').click()
        text = driver.page_source
        # alerttext = driver.switch_to.alert.text
        # print(alerttext)
        # text = driver.find_element(By.CLASS_NAME,value='el-message__content').text
        '''<div role="alert" class="el-message el-message--error is-center" style="top: 20px; z-index: 2019;"><i class="el-message__icon el-icon-error"></i><p class="el-message__content">請輸入用戶名</p><!----></div>'''
        print(text)
        assert '立即查看'
        time.sleep(10)