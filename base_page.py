from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
    
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
            element)
        element.click()
        return element