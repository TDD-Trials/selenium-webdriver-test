from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def navigatePython():
    global driver
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    driver.get("http://python.org")

    driver.maximize_window()

    # while(True):
    #     pass


if __name__ == "__main__":
    navigatePython()