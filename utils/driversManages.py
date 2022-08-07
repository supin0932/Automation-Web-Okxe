from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOpt
from selenium.webdriver.firefox.options import Options as firefoxOpt
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser):
    if browser == 'Firefox':
        driver = firefox_driver_init()
    elif browser == "Edge":
        driver = edge_driver_init()
    else:
        driver = chrome_driver_init()
    return driver


def chrome_driver_init():
    opt = chromeOpt()
    opt.headless = True
    opt.add_argument("--start-maximized")
    driver = webdriver.Chrome("/Users/okxe/Desktop/Automation-Web-Okxe/driver/ChromeDriver/chromedriver", options=opt)

    # driver.implicitly_wait(30)
    # driver.maximize_window()

    print('Open Chrome browser')
    return driver


def firefox_driver_init():
    options = firefoxOpt()
    driver = webdriver.Chrome("C:\Program Files\Mozilla Firefox\geckodriver.exe", options=options)

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open Firefox browser')
    return driver


def edge_driver_init():
    driver = webdriver.Edge(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open Edge browser')
    return driver



