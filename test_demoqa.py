import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from home_page import HomePage

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver

def test_complete_checkbox_interaction(driver):
    # Инициализация HomePage и открытие домашней страницы
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert "https://demoqa.com/" in driver.current_url , \
            "Сайт не открыт."
    # Переход к странице элементов и затем к странице чекбоксов
    elements_page = home_page.go_to_elements_page()
    assert "https://demoqa.com/elements" in driver.current_url , \
            "Сайт не открыт."
    check_box_page = elements_page.go_to_check_box_page()
    assert "https://demoqa.com/checkbox" in driver.current_url, \
            "Страница Check не открыта."
    # Интерактивные действия с чекбоксами
    # Для Home
    home_svg_class = check_box_page.click_to_toggle_Home_check_box()
    assert 'open' in home_svg_class, "Home checkbox did not toggle"
    # Для Downloads
    downloads_svg_class = check_box_page.click_to_toggle_Donwloads_check_box()
    assert 'open' in downloads_svg_class, "Downloads checkbox did not toggle"
    # Для Word File
    result = check_box_page.click_to_Word_File_chek_box()
    assert "You have selected :\nwordFile" in result, "Word File checkbox was not selected properly"
