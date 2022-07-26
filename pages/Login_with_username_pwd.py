from locators.loginLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_with_username_pw:
    def __init__(self, driver):
        self.driver = driver

    def click_button_login(self):
        print('Click login')
        wait = WebDriverWait(self.driver, 30)
        click_login = wait.until(EC.element_to_be_clickable((By.ID, get_button_login_id())))
        click_login.click()

    def click_username(self):
        print('Click username')
        wait = WebDriverWait(self.driver, 30)
        click_username = wait.until(EC.element_to_be_clickable((By.XPATH, get_username_xpath())))
        click_username.click()

    def enter_username(self, username):
        print('Enter username')
        wait = WebDriverWait(self.driver, 30)
        enter_username = wait.until(EC.element_to_be_clickable((By.XPATH, get_username_xpath())))
        enter_username.clear()
        enter_username.send_keys(username)

    def click_pwd(self):
        wait = WebDriverWait(self.driver, 30)
        print('Click password')
        click_password = wait.until(EC.element_to_be_clickable((By.XPATH, get_password_xpath())))
        click_password.click()

    def enter_pwd(self, pwd):
        wait = WebDriverWait(self.driver, 30)
        print('Enter password')
        enter_password = wait.until(EC.element_to_be_clickable((By.XPATH, get_password_xpath())))
        enter_password.clear()
        enter_password.send_keys(pwd)

    def enter_login(self):
        wait = WebDriverWait(self.driver, 30)
        print('Enter login')
        enter_login = wait.until(EC.element_to_be_clickable((By.XPATH, get_button_enter_login_xpath())))
        enter_login.click()

    def click_icon_account(self):
        wait = WebDriverWait(self.driver, 30)
        print('Click icon account')
        click_icon_account = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_icon_account_css())))
        click_icon_account.click()

    def get_username_account(self):
        wait = WebDriverWait(self.driver, 30)
        print('Get username')
        get_username = wait.until(EC.element_to_be_clickable((By.XPATH, get_usernameaccount_xpath()))).text
        return get_username


