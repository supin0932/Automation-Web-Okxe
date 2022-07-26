import pytest
import unittest
import time
from utils.infoLogin import get_url_web
from pages.Login_with_link import LoginPage
from pages.Login_with_username_pwd import Login_with_username_pwd
from pages.Logout import LogoutPage
from utils.driversManages import get_driver
from config.envConfig import EnvConfig
from utils.driversManages import *
from selenium import webdriver
from pages.Register_account import *

# @pytest.mark.usefixtures("driver-class")
@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest2(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()

        self.url = get_url_web()
        self.driver.get(self.url)
        self.login_obj = LoginPage(self.driver)
        self.login_obj1 = Login_with_username_pwd(self.driver)
        self.login_obj2 = RegisterAccount(self.driver)
        envConfig: EnvConfig = EnvConfig.getInstance()
        self.user_name = envConfig.infoLogin.user_name
        self.pwd = envConfig.infoLogin.pwd
        self.pin = envConfig.infoLogin.pin

    def tearDown(self):
        self.driver.quit()

    def login_event(self):
        try:
            self.login_obj.click_button_login()
            # Wait load page
            time.sleep(1)

        except Exception as err:
            print("Login unsuccessfully", err)


    def test_register_account_with_info_correct(self):
        """

        Register account with
        username : True
        passwword : True
        expected : success

        """
        self.login_event()
        self.login_obj2.click_register_button()
        self.login_obj.enter_numberphone("0932757595")
        self.login_obj.click_continue_button()
        self.login_obj2.enter_username_register("nhut1187")
        self.login_obj2.enter_pwd_register("@A123456")
        self.login_obj2.enter_pwd_register_confirm("@A123456")
        self.login_obj2.click_register()
        self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')
        time.sleep(5)
        get_url = self.driver.current_url
        print(get_url)
        if get_url == "https://www.okxe.vn/":
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

    def test_register_account_with_info_uncorrect(self):
        """

        Register account with
        username : True
        passwword : False
        expected : unsuccess

        """
        self.login_event()
        self.login_obj2.click_register_button()
        self.login_obj.enter_numberphone("0932757595")
        self.login_obj.click_continue_button()
        self.login_obj2.enter_username_register("nhut1187")
        self.login_obj2.enter_pwd_register("A123456")
        self.login_obj2.enter_pwd_register_confirm("A123456")
        self.login_obj2.click_register()
        try:
            self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')

        except Exception as ex:
            pass

        time.sleep(5)
        get_url = self.driver.current_url
        print(get_url)
        if get_url != "https://www.okxe.vn/":
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

    def test_register_account_with_info_uncorrect1(self):
        """

        Register account with
        username : False
        passwword : False
        expected : unsuccess

        """
        self.login_event()
        self.login_obj2.click_register_button()
        self.login_obj.enter_numberphone("0932757595")
        self.login_obj.click_continue_button()
        self.login_obj2.enter_username_register("nhut")
        self.login_obj2.enter_pwd_register("A123456")
        self.login_obj2.enter_pwd_register_confirm("A123456")
        self.login_obj2.click_register()
        try:
            self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')

        except Exception as ex:
            pass

        time.sleep(5)
        get_url = self.driver.current_url
        print(get_url)
        if get_url != "https://www.okxe.vn/":
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

    def test_register_account_with_info_uncorrect2(self):
        """

        Register account with
        username : False
        passwword : True
        expected : unsuccess

        """
        self.login_event()
        self.login_obj2.click_register_button()
        self.login_obj.enter_numberphone("0932757595")
        self.login_obj.click_continue_button()
        self.login_obj2.enter_username_register("nhut")
        self.login_obj2.enter_pwd_register("@A123456")
        self.login_obj2.enter_pwd_register_confirm("@A123456")
        self.login_obj2.click_register()
        try:
            self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')

        except Exception as ex:
            pass

        time.sleep(5)
        get_url = self.driver.current_url
        print(get_url)
        if get_url != "https://www.okxe.vn/":
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

    def test_register_account_with_info_empty(self):
        """

        Register account with
        username : Empty
        passwword : Empty
        expected : unsuccess

        """
        self.login_event()
        self.login_obj2.click_register_button()
        self.login_obj.enter_numberphone("0932757595")
        self.login_obj.click_continue_button()
        self.login_obj2.enter_username_register("")
        self.login_obj2.enter_pwd_register("")
        self.login_obj2.enter_pwd_register_confirm("")
        self.login_obj2.click_register()
        try:
            self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')

        except Exception as ex:
            pass

        time.sleep(5)
        get_url = self.driver.current_url
        print(get_url)
        if get_url != "https://www.okxe.vn/":
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False


if __name__ == "__main__":
    unittest.main()
