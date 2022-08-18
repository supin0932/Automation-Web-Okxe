import pytest
import unittest
from pages.Login_with_username_pwd import Login_with_username_pw
from config.envConfig import EnvConfig
from pages.Login_with_link import *
from utils.driversManages import get_driver, chrome_driver_init
from utils.infoLogin import get_url_web_okxe


@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class Login_with_link_Test(unittest.TestCase):

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
            wait = WebDriverWait(self.driver, 30)
            click_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > button")))
            click_login.click()
            self.login_obj.click_button_login()
            # Wait load page
            time.sleep(1)
        except Exception as err:
            print("Login unsuccessfully", err)



    def test_login_with_fb_with_account_unlogined(self):
        """
        Step 1 : Open web OKXE
        Step 2 : Click button login
        Step 3 : Click button link with facebook
        Step 4 : Login account facebook
        Step 5 : Get info account
        Step 7 : Logout account okxe
        Step 8 : Open web Facebook
        Step 9 : Logout account facebook
        Step 10 : Verify info account
        *************************
        Data : + Account facebook : Correct
        Expected Result : Login successfull
        """
        self.driver.switch_to.window(self.window_st1)
        time.sleep(2)
        login_page = str
        self.login_event()
        main_page = self.driver.current_window_handle
        self.login_obj1.click_icon_facebook()

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)
        time.sleep(2)
        self.login_obj1.enter_username_facebook(username='m.nhutle@okxe.vn')
        time.sleep(1)
        self.login_obj1.enter_password_facebook(pwd='@Aa246357')
        time.sleep(1)
        self.login_obj1.click_login_facebook()
        self.driver.switch_to.window(main_page)
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        if text == "Lê Nhựt":
            assert True
        else:
            assert False

    def test_login_with_account_facebook_logined(self):
        """
        Step 1 : Open web Facebook
        Step 2 : Login account facebook
        Step 3 : Open app OKXE
        Step 4 : Click button login
        Step 5 : Click button link with facebook
        Step 6 : Select account facebook
        Step 7 : Get info account
        Step 8 : Logout account okxe
        Step 9 : Logout account facebook
        Step 10 : Verify info account
        *************************
        Data : + Account facebook : Correct
        Expected Result : Login successfull
        """
        self.driver.switch_to.window(self.window_st2)
        time.sleep(3)
        self.login_obj1.enter_username_facebook(username='m.nhutle@okxe.vn') #bug
        self.login_obj1.enter_password_facebook(pwd='@Aa246357')
        time.sleep(3)
        click = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")))
        click.click()
        time.sleep(5)
        self.driver.switch_to.window(self.window_st1)
        time.sleep(2)
        self.login_event()
        click = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/button[1]")))
        click.click()
        self.login_obj.click_icon_account()
        text = self.login_obj.get_username_account()
        if text == "Lê Nhựt":
            assert True
        else:
            assert False


    def test_login_with_gmail_with_account_unlogined(self):
        """
        Step 1 : Open web OKXE
        Step 2 : Click button login
        Step 3 : Click button link with gmail
        Step 4 : Login account gmail
        Step 5 : Get info account
        Step 7 : Logout account okxe
        Step 8 : Open app Gmail
        Step 9 : Logout account gmail
        Step 10 : Verify info account
        *************************
        Data : + Account gmail : Correct
        Expected Result : Login successfull
        """
        self.driver.switch_to.window(self.window_st1)
        time.sleep(2)
        login_page = str
        self.login_event()
        main_page = self.driver.current_window_handle
        click = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/button[2]")))
        click.click()

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("m.nhutle@okxe.vn")
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "password").send_keys("Nhut1176")
        time.sleep(5)
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
        self.driver.save_screenshot('/Users/okxe/Downloads/test.png')
        self.driver.switch_to.window(main_page)
        time.sleep(5)
        self.login_obj.click_icon_account()
        time.sleep(2)
        text = self.login_obj.get_username_account()
        self.driver.save_screenshot('/Users/okxe/Downloads/test1.png')
        if text == "nhut le":
            assert True
        else:
            assert False

    def test_login_with_gmail_with_account_logined(self):
        """
        Step 1 : Open web Gmail
        Step 2 : Login account gmail
        Step 3 : Open app OKXE
        Step 4 : Click button login
        Step 5 : Click button link with gmail
        Step 6 : Select account gmail
        Step 7 : Get info account
        Step 8 : Logout account okxe
        Step 9 : Logout account gmail
        Step 10 : Verify info account
        *************************
        Data : + Account gmail : Correct
        Expected Result : Login successfull
        """
        self.driver.switch_to.window(self.window_st3)
        time.sleep(3)
        self.login_obj1.enter_username_gmail(username='m.nhutle@okxe.vn')
        self.driver.save_screenshot('/Users/okxe/Downloads/screen_shot.png')
        time.sleep(5)
        try:
            self.driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
        except:
            pass
        self.driver.find_element(By.ID, "password").send_keys("Nhut1176")
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

        self.driver.switch_to.window(self.window_st1)
        self.login_event()
        main_page = self.driver.current_window_handle
        click = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/button[2]")))
        click.click()
        login_page = str
        self.driver.save_screenshot('/Users/okxe/Downloads/screen_shot_11.png')
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)

        self.driver.find_element(By.XPATH, "//*[contains(text(),'Lê Minh Nhựt')]").click()
        self.driver.save_screenshot('/Users/okxe/Downloads/screen_shot_12.png')
        self.driver.switch_to.window(main_page)
        time.sleep(6)
        self.driver.save_screenshot('/Users/okxe/Downloads/screen_shot_14.png')
        self.login_obj.click_icon_account()
        self.driver.save_screenshot('/Users/okxe/Downloads/screen_shot_13.png')
        time.sleep(5)
        text = self.login_obj.get_username_account()

        if text == "nhut le":
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
