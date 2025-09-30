from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # если нужен безголовый режим
    
    # Указываем уникальный путь для профиля Chrome, чтобы избежать ошибки с уже используемым профилем
    # options.add_argument("--user-data-dir=C:/tmp/selenium_profile")

    driver = webdriver.Chrome(options=options)  # НЕ указываем Service и путь вручную
    driver.maximize_window()
    yield driver
    driver.quit()
