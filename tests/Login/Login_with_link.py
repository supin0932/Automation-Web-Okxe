import pytest
import unittest
import time
from utils.infoLogin import *
from pages.Login_with_username_pwd import Login_with_username_pw
from pages.Logout import LogoutPage
from config.envConfig import EnvConfig
from utils.driversManages import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.Login_with_link import *
from pages.Login_with_link import *

@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest(unittest.TestCase):

    def setUp(self):

        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()

        self.url_okxe = get_url_web_okxe()
        self.driver.get(self.url_okxe)
        self.window_st1 = self.driver.window_handles[0]
        self.driver.execute_script("window.open('https://facebook.com/','secondtab');")
        self.window_st2 = self.driver.window_handles[1]
        self.driver.execute_script("window.open('https://gmail.com/','thirsttab');")
        self.window_st3 = self.driver.window_handles[2]

        self.login_obj = Login_with_username_pw(self.driver)
        self.login_obj1 = LoginPage(self.driver)

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



    def test_login_with_account_facebook_unlogin(self):
        """

        Login with facebook account
        Number phone verified
        Expected : Login unsuccessfully

        """
        self.driver.switch_to.window(self.window_st1)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[41]/div/button").click()
        login_page = str
        self.login_event()
        main_page = self.driver.current_window_handle
        self.login_obj1.click_icon_facebook()

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)
        time.sleep(2)
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

    def test_login_with_account_facebook_unlogined(self):
        """

        Login with facebook account
        Number phone verified
        Expected : Login unsuccessfully

        """
        self.driver.switch_to.window(self.window_st2)
        self.login_obj1.enter_username_facebook(username='0932241574')
        self.login_obj1.enter_password_facebook(pwd='Nhut1176')
        time.sleep(3)
        # click login facebook
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(5)
        # #click avatar fb
        # self.driver.find_element_by_css_selector(".j83agx80 > .oajrlxb2 > .q9uorilb g").click()
        # time.sleep(5)
        # #click button logout
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]").click()
        # time.sleep(1000)
        self.driver.switch_to.window(self.window_st1)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[41]/div/button").click()
        self.login_event()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/button[1]").click()
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        if text == "Lê Minh Nhựt":
            assert True
        else:
            assert False


    def test_login_with_account_google_numberphone_unlogin(self):
        """

        Login with google account
        Number phone verified
        Expected : Login unsuccessfully

        """
        self.driver.switch_to.window(self.window_st1)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[41]/div/button").click()
        login_page = str
        self.login_event()
        main_page = self.driver.current_window_handle
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/button[2]").click() #click icon gmail

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

    def test_login_with_account_google_numberphone_logined(self):
        """

        Login with google account
        Number phone verified
        Expected : Login unsuccessfully

        """
        self.driver.switch_to.window(self.window_st3)
        self.driver.find_element(By.CSS_SELECTOR, ".button--mobile-before-hero-only").click()  # click button login gmail

        self.login_obj1.enter_username_gmail(username='m.nhutle@okxe.vn')
        self.login_obj1.click_continue_login_gm_button()
        self.login_obj1.enter_password_gmail(pwd='Nhut1176')
        # time.sleep(3000)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click() #click button next pwd
        self.driver.switch_to.window(self.window_st1)
        main_page = self.driver.current_window_handle
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[41]/div/button").click()
        self.login_event()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/button[2]").click() #click icon gmail
        login_page = str

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)
        # chọn account gmail
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div").click()

        self.driver.switch_to.window(main_page)
        time.sleep(10)
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        if text == "Lê Minh Nhựt":
            assert True
        else:
                assert False



    # def test_login_with_account_apple_numberphone_verify(self):
    #     """
    #
    #     Login with apple account
    #     Number phone verified
    #
    #     """
    #     self.driver.switch_to.window(self.window_st1)
    #     login_page = str
    #     self.login_event()
    #     main_page = self.driver.current_window_handle
    #     self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/button[3]").click()
    #     for handle in self.driver.window_handles:
    #         if handle != main_page:
    #             login_page = handle
    #
    #     self.driver.switch_to.window(login_page)
    #     self.login_obj1.enter_usr_apple(username="m.nhutle@okxe.vn")
    #     self.login_obj1.click_login_apple()
    #     self.driver.find_element_by_css_selector(".shared-icon").click()
    #     self.login_obj1.enter_pwd_apple(pwd="@Aa246357")
    #     self.driver.find_element_by_css_selector(".shared-icon").click()
    #     self.login_obj1.click_login_apple()
    #     time.sleep(5000)
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
