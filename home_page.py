from selenium.webdriver.common.by import By
from base_page import BasePage
from elements_page import ElementsPage

class HomePage(BasePage):
    HOME_PAGE_URL = "https://demoqa.com/"
    ELEMENTS_CARD = (By.CSS_SELECTOR, '[viewBox="0 0 448 512"]')

    def open_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)
        assert "https://demoqa.com/" in self.driver.current_url , \
            "Сайт не открыт."
        return HomePage(self.driver)

    def go_to_elements_page(self):
        self.click_element(self.ELEMENTS_CARD)
        assert "https://demoqa.com/elements" in self.driver.current_url, \
            "Страница Elements не открыта."
        return ElementsPage(self.driver)

    