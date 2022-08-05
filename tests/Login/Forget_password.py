import pytest
import unittest
import time
from utils.infoLogin import get_url_web_okxe
from pages.Login_with_link import LoginPage
from pages.Login_with_username_pwd import Login_with_username_pw
from pages.Logout import LogoutPage
from config.envConfig import EnvConfig
from utils.driversManages import *
from pages.Register_account import *
from pages.Forget_id_and_pwd import *

# @pytest.mark.usefixtures("driver-class")
@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest3(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()

        self.url_okxe = get_url_web_okxe()
        self.driver.get(self.url_okxe)
        self.window_st1 = self.driver.window_handles[0]
        self.driver.execute_script("window.open('https://gmail.com/','secondtab');")
        self.window_st2 = self.driver.window_handles[1]


        self.login_obj = Login_with_username_pw(self.driver)
        self.login_obj1 = LoginPage(self.driver)

        envConfig: EnvConfig = EnvConfig.getInstance()
        self.user_name = envConfig.infoLogin.user_name
        self.pwd = envConfig.infoLogin.pwd
        self.pin = envConfig.infoLogin.pin

    def tearDown(self):
        self.driver.quit()


    def test_forget_password(self):
        """

        Forget password with
        Number phone : True
        Expected : success

        """
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[41]/div/button").click()
        self.login_obj.click_button_login()
        self.login_obj3.click_button_forget_pwd()
        self.login_obj1.enter_numberphone("0932241574")
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[1]/div[3]/div/div/div[4]/button").click()
        time.sleep(20)
        # self.login_obj.enter_otp(n1='6', n2='9', n3='6', n4='9', n5='6', n6='9')
        # self.login_obj3.click_tab_pwd()
        # self.login_obj3.enter_pwd_fg("@Nhut1177")
        # self.login_obj3.enter_pwd_fg_cf("@Nhut1177")
        # self.login_obj3.click_button_confirm()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector(".v-btn--block > .v-btn__content").click()
        # self.login_obj3.click_button_back_login()
        # self.login_obj1.enter_username("0932949905")
        # self.login_obj1.enter_pwd("@Nhut1177")
        # self.login_obj1.enter_login()
        # get_url = self.driver.current_url
        # print(get_url)
        # if get_url == "https://www.okxe.vn/":
        #     self.driver.quit()
        #     assert True
        # else:
        #     self.driver.quit()
        #     assert False


if __name__ == "__main__":
    unittest.main()
