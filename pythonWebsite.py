from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def navigatePython():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    driver.get("http://python.org")

    driver.maximize_window()

    # get the search bar element by name
    element = driver.find_element(by=By.NAME, value="q")

    # clear the search bar and enter Pycon and search
    element.clear()
    element.send_keys("ytteadjsajfkh")
    element.send_keys(Keys.RETURN)

    assert  "No results found." not in driver.page_source

    while(True):
        pass


if __name__ == "__main__":
    navigatePython()