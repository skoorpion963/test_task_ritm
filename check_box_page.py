from selenium.webdriver.common.by import By
from base_page import BasePage

class CheckBoxPage(BasePage):
    CHECK_BOX_CARD = (By.CSS_SELECTOR, 'viewBox="0 0 1024 1024')
    TOGGLE_HOME = (By.XPATH, 
            '//*[@id="tree-node"]/ol/li/span/button')
    TOGGLE_DONWLOADS = (By.XPATH, 
            '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
    WORD_FILE = (By.XPATH, 
    '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]')
    RESULT = (By.XPATH ,"""//*[@id="result"]""")

    def svg_class_name(self, element):
        svg_element = element.find_element(By.TAG_NAME ,'svg')
        svg_class = svg_element.get_attribute('class')
        return svg_class

    def go_to_check_box_page(self):
        self.click_element(self.CHECK_BOX_CARD)
        assert "https://demoqa.com/checkbox" in self.driver.current_url, \
            "Страница Check Box не открыта."
        return CheckBoxPage(self.driver)

    def click_to_toggle_Home_check_box(self):
        element = self.click_element(self.TOGGLE_HOME)
        svg_class = self.svg_class_name(element)
        assert 'open' in svg_class , "Директория Home не раскрыта"
        return CheckBoxPage(self.driver)

    def click_to_toggle_Donwloads_check_box(self):
        element = self.click_element(self.TOGGLE_DONWLOADS)
        svg_class = self.svg_class_name(element)
        assert 'open' in svg_class , "Директория Home не раскрыта"
        return CheckBoxPage(self.driver)

    def click_to_Word_File_chek_box(self):
        self.click_element(self.WORD_FILE)

        return CheckBoxPage(self.driver)
    
    def check_result(self):
        result = self.wait_for_element(self.RESULT)
        result = result.text
        assert "You have selected :\nwordFile" in result , \
            "Сообщение не появилось"
        

