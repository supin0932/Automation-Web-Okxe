from locators.loginLocator import *


class RegisterAccount:
    def __init__(self, driver):
        self.driver = driver

    def click_register_button(self):
        print("Click register button")
        click_rg_bt = self.driver.find_element_by_xpath(get_button_register_xpath())
        click_rg_bt.click()

    def click_username_register(self):
        print("Click username register")
        click_usr_rg = self.driver.find_element_by_xpath(get_usr_register_xpath())
        click_usr_rg.click()

    def enter_username_register(self, username):
        print("Enter username register")
        enter_usr_rg = self.driver.find_element_by_xpath(get_usr_register_xpath())
        enter_usr_rg.clear()
        enter_usr_rg.send_keys(username)

    def click_pwd_register(self):
        print("Click password register")
        click_pwd_rg = self.driver.find_element_by_xpath(get_pwd_register_xpath())
        click_pwd_rg.click()

    def enter_pwd_register(self, pwd):
        print("Enter password register")
        enter_pwd_rg = self.driver.find_element_by_xpath(get_pwd_register_xpath())
        enter_pwd_rg.clear()
        enter_pwd_rg.send_keys(pwd)

    def click_pwd_register_confirm(self):
        print("Click password register confirm")
        click_pwd_rg_cf = self.driver.find_element_by_css_selector(get_pwd_register_confirm_css())
        click_pwd_rg_cf.click()

    def enter_pwd_register_confirm(self, pwd):
        print("Enter password register confirm")
        enter_pwd_rg = self.driver.find_element_by_css_selector(get_pwd_register_confirm_css())
        enter_pwd_rg.clear()
        enter_pwd_rg.send_keys(pwd)

    def click_register(self):
        print("Click register")
        click_rg = self.driver.find_element_by_xpath(get_register_button_xpath())
        click_rg.click()

