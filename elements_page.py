from selenium.webdriver.common.by import By
from base_page import BasePage
from check_box_page import CheckBoxPage

class ElementsPage(BasePage):
    CHECK_BOX_MENU_ITEM = (By.XPATH, "//*[contains(text(),'Check Box')]")

    def go_to_check_box_page(self):
        self.wait_for_element(self.CHECK_BOX_MENU_ITEM).click()
        return CheckBoxPage(self.driver)