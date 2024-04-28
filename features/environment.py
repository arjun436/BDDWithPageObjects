import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from utilities import configReader


def before_scenario(context, driver):
    if configReader.readConfig("basic info","browser") == "chrome":
        service = Service(executable_path=ChromeDriverManager().install(), service_args=["--verbose", "--log-path=cd.log"])
        context.driver = webdriver.Chrome(service=service)
    if configReader.readConfig("basic info","browser") == "firefox":
        service = Service(executable_path=GeckoDriverManager().install(), service_args=["--verbose", "--log-path=cd.log"])
        context.driver = webdriver.Firefox(service=service)
    if configReader.readConfig("basic info","browser") == "edge":
        service = Service(executable_path=EdgeChromiumDriverManager().install(), service_args=["--verbose", "--log-path=cd.log"])
        context.driver = webdriver.Edge(service=service)
        


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
