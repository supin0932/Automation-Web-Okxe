import pytest
import unittest
import time
from OKXE.utils.infoLogin import get_url_web
from OKXE.pages.Login_with_username_pwd import Login_with_username_pw
from OKXE.pages.Logout import LogoutPage
from OKXE.config.envConfig import EnvConfig
from OKXE.utils.driversManages import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from OKXE.pages.Login_with_link import *


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
        self.login_obj1 = LoginPage(self.driver)

        envConfig: EnvConfig = EnvConfig.getInstance()
        self.user_name = envConfig.infoLogin.user_name
        self.pwd = envConfig.infoLogin.pwd
        self.pin = envConfig.infoLogin.pin


    def tearDown(self):
        ""
        # self.driver.close()

    def login_event(self):
        try:
            self.login_obj.click_button_login()
            # Wait load page
            time.sleep(1)

        except Exception as err:
            print("Login unsuccessfully", err)



    def test_login_with_account_facebook_numberphone_veryfied(self):
        """

        Login with facebook account
        Number phone verified
        Expected : Login unsuccessfully

        """
        login_page = str
        self.login_event()
        main_page = self.driver.current_window_handle
        self.login_obj1.click_icon_facebook()

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)

        self.login_obj1.enter_username_facebook(username='0932241574')
        time.sleep(1)
        self.login_obj1.enter_password_facebook(pwd='Nhut1176')
        time.sleep(1)
        self.login_obj1.click_login_facebook()
        self.driver.switch_to.window(main_page)
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        if text == "Lê Minh Nhựt":
            assert True
        else:
            assert False

    # def test_login_with_account_facebook_numberphone_unverify(self):
    #     """
    #
    #     Login with facebook account
    #     Number phone unverify
    #
    #     """
    #     login_page = str
    #     self.login_event()
    #     main_page = self.driver.current_window_handle
    #     print(self.driver.current_url)
    #     self.login_obj.click_icon_facebook()
    #
    #     for handle in self.driver.window_handles:
    #         if handle != main_page:
    #             login_page = handle
    #
    #     self.driver.switch_to.window(login_page)
    #
    #     self.login_obj.enter_username_facebook(username='mbjzcxbeje_1655970496@tfbnw.net')
    #     time.sleep(1)
    #     self.login_obj.enter_password_facebook(pwd='dfglkdfjg45gdflkgjfd')
    #     time.sleep(1)
    #     self.login_obj.click_login_facebook()
    #     # self.login_obj.click_link_facebook()
    #     try:
    #         self.login_obj.click_link_facebook()
    #     except:
    #         print("Account linked")
    #     finally:
    #         self.driver.switch_to.window(main_page)
    #     self.login_obj.click_veryfi_numberphone()
    #     self.login_obj.enter_numberphone(number='0339957452')
    #     self.login_obj.click_continue_button()
    #     self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')
    #     time.sleep(2)
    #     get_url = self.driver.current_url
    #     print(get_url)
    #     if get_url == "https://www.okxe.vn/":
    #         self.driver.quit()
    #         assert True
    #     else:
    #         self.driver.quit()
    #         assert False

    def test_login_with_account_google_numberphone_verify(self):
        """

        Login with google account
        Number phone verified
        Expected : Login unsuccessfully

        """
        login_page = str
        self.login_event()
        main_page = self.driver.current_window_handle
        print(self.driver.current_url)
        self.login_obj1.click_icon_gmail()

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)
        self.login_obj1.enter_username_gmail(username="m.nhutle@okxe.vn")
        self.login_obj1.click_continue_pwd_button()
        self.login_obj1.enter_password_gmail(pwd="Nhut1176")
        self.login_obj1.click_continue_pwd_button()
        self.driver.switch_to.window(main_page)
        time.sleep(10)
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        if text == "Lê Minh Nhựt":
            assert True
        else:
            assert False


    # def test_login_with_account_google_numberphone_unverify(self):
    #     """
    #
    #     Login with google account
    #     Number phone unverified
    #
    #     """
    #     login_page = str
    #     self.login_event()
    #     main_page = self.driver.current_window_handle
    #     print(self.driver.current_url)
    #     self.login_obj.click_icon_gmail()
    #
    #     for handle in self.driver.window_handles:
    #         if handle != main_page:
    #             login_page = handle
    #
    #     self.driver.switch_to.window(login_page)
    #     self.login_obj.enter_username_gmail(username="m.nhutle@okxe.vn")
    #     self.login_obj.click_continue_pwd_button()
    #     self.login_obj.enter_password_gmail(pwd="Nhut1176")
    #     self.login_obj.click_continue_login_gm_button()
    #     self.driver.switch_to.window(main_page)
    #     self.login_obj.click_veryfi_numberphone()
    #     self.login_obj.enter_numberphone(number='0339957452')
    #     self.login_obj.click_continue_button()
    #     self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')
    #     time.sleep(2)
    #     get_url = self.driver.current_url
    #     print(get_url)
    #     if get_url == "https://www.okxe.vn/":
    #         self.driver.quit()
    #         assert True
    #     else:
    #         self.driver.quit()
    #         assert False

    # def test_login_with_account_apple_numberphone_verify(self):
    #     """
    #
    #     Login with apple account
    #     Number phone verified
    #
    #     """
    #     login_page = str
    #     self.login_event()
    #     main_page = self.driver.current_window_handle
    #     print(self.driver.current_url)
    #     self.login_obj.click_icon_apple()
    #
    #     for handle in self.driver.window_handles:
    #         if handle != main_page:
    #             login_page = handle
    #
    #     self.driver.switch_to.window(login_page)
    #     self.login_obj.enter_usr_apple(username="alo")
    #     self.login_obj.click_login_apple()
    #     self.driver.find_element_by_css_selector(".shared-icon").click()
    #     self.login_obj.enter_pwd_apple(pwd="alo")
    #     self.driver.find_element_by_css_selector(".shared-icon").click()
    #     self.login_obj.click_login_apple()
    #     time.sleep(2)
    #     get_url = self.driver.current_url
    #     print(get_url)
    #     if get_url == "https://www.okxe.vn/":
    #         self.driver.quit()
    #         assert True
    #     else:
    #         self.driver.quit()
    #         assert False
    #
    # def test_login_with_account_apple_numberphone_unverify(self):
    #     """
    #
    #     Login with apple account
    #     Number phone unverified
    #
    #     """
    #     login_page = str
    #     self.login_event()
    #     main_page = self.driver.current_window_handle
    #     print(self.driver.current_url)
    #     self.login_obj.click_icon_apple()
    #
    #     for handle in self.driver.window_handles:
    #         if handle != main_page:
    #             login_page = handle
    #
    #     self.driver.switch_to.window(login_page)
    #     self.login_obj.enter_usr_apple(username="alo")
    #     self.login_obj.click_login_apple()
    #     self.driver.find_element_by_css_selector(".shared-icon").click()
    #     self.login_obj.enter_pwd_apple(pwd="alo")
    #     self.driver.find_element_by_css_selector(".shared-icon").click()
    #     self.login_obj.click_login_apple()
    #     self.driver.switch_to.window(main_page)
    #     self.login_obj.click_veryfi_numberphone()
    #     self.login_obj.enter_numberphone(number='0339957452')
    #     self.login_obj.click_continue_button()
    #     self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')
    #     time.sleep(2)
    #     get_url = self.driver.current_url
    #     print(get_url)
    #     if get_url == "https://www.okxe.vn/":
    #         self.driver.quit()
    #         assert True
    #     else:
    #         self.driver.quit()
    #         assert False


if __name__ == "__main__":
    unittest.main()
