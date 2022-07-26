from locators.loginLocator import *


class ForgetPassword:
    def __init__(self, driver):
        self.driver = driver

    def click_button_forget_pwd(self):
        print("Click forget password")
        click_fg_pwd = self.driver.find_element_by_xpath(get_forget_pwd_button_xpath())
        click_fg_pwd.click()

    def click_tab_pwd(self):
        print("Click tab password")
        click_tb_pwd = self.driver.find_element_by_css_selector(get_tab_pwd_css())
        click_tb_pwd.click()

    def click_pwd_fg(self):
        print("Click password forget")
        click_pwd_fg = self.driver.find_element_by_css_selector(get_fg_pwd_css())
        click_pwd_fg.click()

    def enter_pwd_fg(self, pwd):
        print("Enter password forget")
        enter_pwd_fg = self.driver.find_element_by_css_selector(get_fg_pwd_css())
        enter_pwd_fg.clear()
        enter_pwd_fg.send_keys(pwd)

    def click_pwd_fg_cf(self):
        print("Click password forget confirm")
        click_pwd_fg_cf = self.driver.find_element_by_css_selector(get_fg_pwd_cf_css())
        click_pwd_fg_cf.click()

    def enter_pwd_fg_cf(self, pwdcf):
        print("Enter password forget")
        enter_pwd_fg_cf = self.driver.find_element_by_css_selector(get_fg_pwd_cf_css())
        enter_pwd_fg_cf.clear()
        enter_pwd_fg_cf.send_keys(pwdcf)

    def click_button_confirm(self):
        print("Click button confirm")
        click_button_cf = self.driver.find_element_by_css_selector(get_button_confirm_css())
        click_button_cf.click()

    def click_button_back_login(self):
        print("Click button back login")
        click_button_back_login = self.driver.find_element_by_xpath(get_button_back_login_xpath())
        click_button_back_login.click()

