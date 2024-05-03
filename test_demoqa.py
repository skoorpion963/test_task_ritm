from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
   

from home_page import HomePage



# Создание экземпляра главной страницы 
home_page = HomePage(driver).open_home_page()

# Переход к элементам 
elements_page = home_page.go_to_elements_page()

# Переход к странице с чекбоксами
check_box_page = elements_page.go_to_check_box_page()

# Работа с директориями и файлами
check_box_page.click_to_toggle_Home_check_box()
check_box_page.click_to_toggle_Donwloads_check_box()
check_box_page.click_to_Word_File_chek_box()
check_box_page.check_result()

# Закрыть браузер после выполнения теста
driver.quit()
