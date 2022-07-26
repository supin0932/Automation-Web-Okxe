import pytest
import unittest
import time
from selenium import webdriver
from utils.infoLogin import get_url_web_okxe
from pages.Login_with_username_pwd import Login_with_username_pw
from pages.Logout import LogoutPage
from config.envConfig import EnvConfig
from utils.driversManages import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest(unittest.TestCase):

    def setUp(self):

        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()

        self.url = get_url_web()
        self.driver.get(self.url)
        self.login_obj = Login_with_username_pw(self.driver)

        envConfig: EnvConfig = EnvConfig.getInstance()
        self.user_name = envConfig.infoLogin.user_name
        self.pwd = envConfig.infoLogin.pwd
        self.pin = envConfig.infoLogin.pin


    def tearDown(self):
        self.driver.close()

    def login_event(self, username, pwd):
        try:
            self.login_obj.click_button_login()

            # Wait load page
            time.sleep(1)

            self.login_obj.enter_username(username)
            self.login_obj.enter_pwd(pwd)
            self.login_obj.enter_login()
            time.sleep(2)

        except Exception as err:
            print("Login unsuccessfully", err)


    def test_login_with_pwd_uncorrect(self):
        """
        Username : True
        Password : False
        Expected : Login unsuccessfully
        """
        self.login_event(username='0932241574', pwd='1111111111')
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Mật khẩu không chính xác, vui lòng kiểm tra lại.":
            assert True
        else:
            assert False

    def test_login_with_username_uncorrect(self):
        """
        Username : False
        Password : True
        Expected : Login unsuccessfully
        """
        self.login_event(username='1111111111', pwd='@Aa246357')
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Mật khẩu không chính xác, vui lòng kiểm tra lại.":
            assert True
        else:
            assert False

    def test_login_with_acc_and_pwd_emtry(self):
        """
        Username : Empty
        Password : Empty
        Expected : Login unsuccessfully
        """
        self.login_event(username="", pwd="")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Thông tin đăng nhập và mật khẩu không được bỏ trống":
            assert True
        else:
            assert False

    def test_login_with_username_emtry(self):
        """
        Username : Empty
        Password : True
        Expected : Login unsuccessfully
        """

        self.login_event(username="", pwd="@Aa246357")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Thông tin đăng nhập và mật khẩu không được bỏ trống":
            assert True
        else:
            assert False

    def test_login_with_pwd_emtry(self):
        """
        Username : True
        Password : Empty
        Expected : Login unsuccessfully
        """

        self.login_event(username="0932949905", pwd="")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Thông tin đăng nhập và mật khẩu không được bỏ trống":
            assert True
        else:
            assert False

    def test_login_with_acc_and_pwd_correct(self):
        """
        Username : True
        Password : True
        Expected : Login successfully
        """
        self.login_event(username="0932241574", pwd="@Aa246357")
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        time.sleep(500)
        if text == "nhut le":
            assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
