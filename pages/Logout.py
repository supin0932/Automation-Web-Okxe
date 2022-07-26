from locators.logoutLocator import *


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_icon_avatar(self):
        print("Click icon avatar")
        click_iconavt = self.driver.find_element_by_xpath(get_icon_avatar_xpath())
        click_iconavt.click()

    def click_icon_setting(self):
        print("Click icon setting")
        click_icon_setting = self.driver.find_element_by_xpath(get_icon_setting_xpath())
        click_icon_setting.click()

    def click_ok(self):
        print("Click button ok")
        click_ok = self.driver.find_element_by_xpath(get_button_ok_xpath())
        click_ok.click()

    def click_cancel(self):
        print("Click button cancel")
        click_cancel = self.driver.find_element_by_id(get_button_cancel_xpath())
        click_cancel.click()

