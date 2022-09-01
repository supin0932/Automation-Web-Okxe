import os
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
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains

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
            click_login = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[58]/div/button/div")))
            click_login.click()
            self.login_obj.click_button_login()
            # Wait load page
            time.sleep(1)
        except Exception as err:
            print("Login unsuccessfully", err)

    def test_forget_password(self):
        """

        """
        wait = WebDriverWait(self.driver, 60)
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "bt_login_box_home_page")))
        click_login.click()
        self.login_obj.enter_username(username="test1234")
        self.login_obj.enter_pwd(pwd="@Aa246357")
        self.login_obj.enter_login()
        click_login1 = wait.until(EC.element_to_be_clickable((By.ID, "register-product_btn-register")))
        click_login1.click()
        time.sleep(3)
        self.driver.execute_script('document.getElementById("register-product_upload-image").style.display = "block"')
        element = wait.until(EC.element_to_be_clickable((By.ID, "register-product_upload-image")))
        element.send_keys('/Users/nhutle/Downloads/multi-browsers.png')
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_next-page")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_input-select-brand")))
        click_login.click()
        time.sleep(5)
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_popular-brand-15")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_search-model")))
        click_login.send_keys('Vision')
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_model-135")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_search-model-detail-318")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_btn-corfirm-brand-model-detail")))
        click_login.click()
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, window.scrollY + 800)')
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_input-select-year")))
        time.sleep(1)
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Jan')]")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_input-select-mileage")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_mileage-40.000")))
        time.sleep(1)
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_input-select-color")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_color-4")))
        time.sleep(1)
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_confirm-selected-color")))
        time.sleep(1)
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_input-select-location")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_search-location")))
        click_login.send_keys("Cần Thơ")
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_location-5")))
        time.sleep(5)
        click_login.click()
        self.driver.execute_script('window.scrollTo(0, window.scrollY + 800)')
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_input-set-price")))
        time.sleep(1)
        click_login.send_keys("2000000")
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_input-description")))
        click_login.send_keys("okxe")
        click_login = wait.until(EC.element_to_be_clickable((By.ID, "register-product_post")))
        click_login.click()
        click_login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "title-success"))).text
        if click_login == "Đăng bán xe thành công!":
            assert True
        else:
            assert False
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()