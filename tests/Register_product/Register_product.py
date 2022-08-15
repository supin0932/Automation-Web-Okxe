from telnetlib import EC

import pytest
import unittest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.infoLogin import *
from pages.Login_with_link import LoginPage
from pages.Login_with_username_pwd import Login_with_username_pw
from pages.Logout import LogoutPage
from config.envConfig import EnvConfig
from utils.driversManages import *
from pages.Register_account import *
from pages.Forget_id_and_pwd import *

# @pytest.mark.usefixtures("driver-class")
@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class ForgetpasswordTest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()

        self.url_okxe = get_url_web_okxe_stage()
        self.driver.get(self.url_okxe)
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
            wait = WebDriverWait(self.driver, 30)
            click_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > button")))
            click_login.click()
            self.login_obj.click_button_login()
            # Wait load page
            time.sleep(1)
        except Exception as err:
            print("Login unsuccessfully", err)

    def test_forget_password(self):
        """

        """
        wait = WebDriverWait(self.driver, 30)
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "bt_login_box_home_page")))
        click_login.click()
        self.login_obj.enter_username(username="test1234")
        self.login_obj.enter_pwd(pwd="@Aa246357")
        self.login_obj.enter_login()
        click_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#register-product_btn-register .v-responsive__content")))
        click_login.click()
        time.sleep(1115)

if __name__ == "__main__":
    unittest.main()