import pytest
import unittest
import time
from utils.infoLogin import get_url_web_okxe
from pages.Login_with_username_pwd import Login_with_username_pw
from config.envConfig import EnvConfig
from utils.driversManages import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class Login_with_account_Test(unittest.TestCase):

    def setUp(self):

        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()

        self.url = get_url_web_okxe()
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
            wait = WebDriverWait(self.driver, 30)
            click_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > button")))
            click_login.click()
            self.login_obj.click_button_login()

            # Wait load page
            time.sleep(1)

            self.login_obj.enter_username(username)
            self.login_obj.enter_pwd(pwd)
            self.login_obj.enter_login()
            time.sleep(2)

        except Exception as err:
            print("Login unsuccessfully", err)


    def test_login_with_usr_is_true_pwd_is_false(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : True
               + Password : False
        Expected : Login unsuccessfully
        """
        self.login_event(username='0932241574', pwd='1111111111')
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Mật khẩu không chính xác, vui lòng kiểm tra lại.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_false_pwd_is_true(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : False
               + Password : True
        Expected : Login unsuccessfully
        """
        self.login_event(username='1111111111', pwd='@Aa246357')
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Mật khẩu không chính xác, vui lòng kiểm tra lại.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_empty_pwd_is_emtry(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : Empty
               + Password : Empty
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
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : True
               + Password : Empty
        Expected : Login unsuccessfully
        """
        self.login_event(username="", pwd="@Aa246357")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Thông tin đăng nhập và mật khẩu không được bỏ trống":
            assert True
        else:
            assert False

    def test_login_with_usr_is_true_pwd_is_emtry(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : True
               + Password : Empty
        Expected : Login unsuccessfully
        """
        self.login_event(username="0932949905", pwd="")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Thông tin đăng nhập và mật khẩu không được bỏ trống":
            assert True
        else:
            assert False

    def test_login_with_usr_is_true_pwd_is_true(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get username
        Step 4 : Logout account
        Step 5 : Compare with expected result
        ***********************
        Data : + Username : True
               + Password : True
        Expected : Login successfully
        """
        self.login_event(username="0932241574", pwd="@Aa246357")
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        if text == "nhut le":
            assert True
        else:
            assert False

    def test_login_with_usr_is_false_pw_is_false(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : False
               + Password : False
        Expected : Login unsuccessfully
        """
        self.login_event(username="093294abc", pwd="12344556")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Tên đăng nhập không tồn tại.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_false_pw_is_empty(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : False
               + Password : Empty
        Expected : Login unsuccessfully
        """
        self.login_event(username="093294abc", pwd="")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Thông tin đăng nhập và mật khẩu không được bỏ trống":
            assert True
        else:
            assert False

    def test_login_with_usr_is_empty_pw_is_false(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        ***********************
        Data : + Username : Empty
               + Password : False
        Expected : Login unsuccessfully
        """
        self.login_event(username="", pwd="1234567")
        get_url = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        if get_url == "Thông tin đăng nhập và mật khẩu không được bỏ trống":
            assert True
        else:
            assert False

if __name__ == "__main__":
    unittest.main()

