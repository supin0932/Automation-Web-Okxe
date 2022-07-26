import time

from selenium.webdriver.common.keys import Keys
from locators.loginLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_button_login(self):
        print('Click login')
        wait = WebDriverWait(self.driver, 30)
        click_login = wait.until(EC.element_to_be_clickable((By.ID, get_button_login_id())))
        click_login.click()


    def click_icon_facebook(self):
        print('Click icon facebook')
        wait = WebDriverWait(self.driver, 30)
        click_iconfacebook = wait.until(EC.element_to_be_clickable((By.XPATH, get_icon_facebook_xpath())))
        click_iconfacebook.click()

    def click_icon_gmail(self):
        print('Click icon gmail')
        wait = WebDriverWait(self.driver, 30)
        click_icongmail =  wait.until(EC.element_to_be_clickable((By.ID, get_icon_gmail_id())))
        click_icongmail.click()

    def click_icon_apple(self):
        print('Click icon apple')
        wait = WebDriverWait(self.driver, 30)
        click_iconapple = wait.until(EC.element_to_be_clickable((By.XPATH, get_icon_apple_xpath())))
        click_iconapple.click()

    def click_username_facebook(self):
        print("Click username facebook")
        wait = WebDriverWait(self.driver, 30)
        click_username_fb = wait.until(EC.element_to_be_clickable((By.XPATH, get_username_facebook_xpath())))
        click_username_fb.click()

    def click_password_facebook(self):
        print("Click password facebook")
        wait = WebDriverWait(self.driver, 30)
        click_password_fb = wait.until(EC.element_to_be_clickable((By.XPATH, get_password_facebook_xpath())))
        click_password_fb.click()

    def enter_username_facebook(self, username):
        print("Enter username facebook")
        wait = WebDriverWait(self.driver, 30)
        enter_username_fb = wait.until(EC.element_to_be_clickable((By.XPATH, get_username_facebook_xpath())))
        enter_username_fb.clear()
        enter_username_fb.send_keys(username)

    def enter_password_facebook(self, pwd):
        print("Enter password facebook")
        wait = WebDriverWait(self.driver, 30)
        enter_password_fb = wait.until(EC.element_to_be_clickable((By.XPATH, get_password_facebook_xpath())))
        enter_password_fb.clear()
        enter_password_fb.send_keys(pwd)


    def click_login_facebook(self):
        print("Click login facebook")
        wait = WebDriverWait(self.driver, 30)
        enter_password_fb = wait.until(EC.element_to_be_clickable((By.XPATH, get_button_login_facebook_xpath())))
        enter_password_fb.click()


    def click_veryfi_numberphone(self):
        print("Click veryfi numberphone")
        wait = WebDriverWait(self.driver, 30)
        click_veryfi_nbf = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_verify_numberphone_button_css())))
        click_veryfi_nbf.click()

    def click_logout(self):
        print("Click logout")
        wait = WebDriverWait(self.driver, 30)
        click_logout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_button_logout_css())))
        click_logout.click()

    def enter_numberphone(self, number):
        print("Enter numberphone")
        wait = WebDriverWait(self.driver, 30)
        enter_nbf = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_numberphone_css())))
        enter_nbf.clear()
        enter_nbf.send_keys(number)

    def click_continue_button(self):
        print("Click continue")
        wait = WebDriverWait(self.driver, 30)
        click_continue = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_continue_button_css())))
        click_continue.click()

    def enter_otp(self, n1, n2, n3, n4, n5, n6):
        print("Enter OTP")
        wait = WebDriverWait(self.driver, 30)
        enter_opt6 = wait.until(EC.element_to_be_clickable((By.XPATH, get_number6_opt_xpath())))
        enter_opt6.clear()
        enter_opt6.send_keys(n6)

        enter_opt1 = wait.until(EC.element_to_be_clickable((By.XPATH, get_number1_opt_xpath())))
        enter_opt1.clear()
        enter_opt1.send_keys(n1)

        enter_opt2 = wait.until(EC.element_to_be_clickable((By.XPATH, get_number2_opt_xpath())))
        enter_opt2.clear()
        enter_opt2.send_keys(n2)

        enter_opt3 = wait.until(EC.element_to_be_clickable((By.XPATH, get_number3_opt_xpath())))
        enter_opt3.clear()
        enter_opt3.send_keys(n3)

        enter_opt4 = wait.until(EC.element_to_be_clickable((By.XPATH, get_number4_opt_xpath())))
        enter_opt4.clear()
        enter_opt4.send_keys(n4)

        enter_opt5 = wait.until(EC.element_to_be_clickable((By.XPATH, get_number5_opt_xpath())))
        enter_opt5.clear()
        enter_opt5.send_keys(n5)

    def click_link_facebook(self):
        print("Click link facebook")
        wait = WebDriverWait(self.driver, 30)
        click_link_fb = wait.until(EC.element_to_be_clickable((By.XPATH, get_click_link_facebook_xpath())))
        click_link_fb.click()

    def click_username_gmail(self):
        print("Click username gmail")
        wait = WebDriverWait(self.driver, 30)
        click_usr_gm = wait.until(EC.element_to_be_clickable((By.ID, get_usr_gmail_id())))
        click_usr_gm.click()

    def enter_username_gmail(self, username):
        print("Enter username gmail")
        wait = WebDriverWait(self.driver, 30)
        enter_usr_gm = wait.until(EC.element_to_be_clickable((By.ID, get_usr_gmail_id())))
        enter_usr_gm.clear()
        enter_usr_gm.send_keys(username)

    def click_password_gmail(self):
        print("Click password gmail")
        wait = WebDriverWait(self.driver, 30)
        click_pwd_gm = wait.until(EC.element_to_be_clickable((By.XPATH, get_pwd_gmail_xpath())))
        click_pwd_gm.click()

    def enter_password_gmail(self, pwd):
        print("Enter password gmail")
        wait = WebDriverWait(self.driver, 30)
        enter_pwd_gm = wait.until(EC.element_to_be_clickable((By.XPATH, get_pwd_gmail_xpath())))
        enter_pwd_gm.clear()
        enter_pwd_gm.send_keys(pwd)

    def click_continue_pwd_button(self):
        print("Click continue button")
        wait = WebDriverWait(self.driver, 30)
        click_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_continue_button_css())))
        click_continue_button.click()

    def click_continue_login_gm_button(self):
        print("Click continue login button")
        wait = WebDriverWait(self.driver, 30)
        click_continue_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, get_continue_login_gmail_button_xpath())))
        click_continue_login_button.click()

    def click_usr_apple(self):
        print("Click username apple")
        wait = WebDriverWait(self.driver, 30)
        click_usr_apple = wait.until(EC.element_to_be_clickable((By.ID, get_usr_apply_id())))
        click_usr_apple.click()

    def enter_usr_apple(self, username):
        print("Enter username apple")
        wait = WebDriverWait(self.driver, 30)
        enter_usr_apple = wait.until(EC.element_to_be_clickable((By.ID, get_usr_apply_id())))
        enter_usr_apple.clear()
        enter_usr_apple.send_keys(username)

    def click_pwd_apple(self):
        print("Click password apple")
        wait = WebDriverWait(self.driver, 30)
        click_pwd_apple = wait.until(EC.element_to_be_clickable((By.ID, get_pwd_apply_id())))
        click_pwd_apple.click()

    def enter_pwd_apple(self, pwd):
        print("Enter password apple")
        wait = WebDriverWait(self.driver, 30)
        enter_pwd_apple = wait.until(EC.element_to_be_clickable((By.ID, get_pwd_apply_id())))
        enter_pwd_apple.clear()
        enter_pwd_apple.send_keys(pwd)

    def click_login_apple(self):
        print("Click login apple")
        wait = WebDriverWait(self.driver, 30)
        click_login_apple = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_login_apply_css())))
        click_login_apple.click()