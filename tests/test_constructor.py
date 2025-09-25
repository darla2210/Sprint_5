import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import TestLocators

class TestConstructorTabs:

    def test_tab_sauce(driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait.until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR)).click()
        active_element = wait.until(EC.visibility_of_element_located(TestLocators.ACTIVE_TAB_SAUCE_LOCATOR))
        assert active_element.is_displayed()

    def test_tab_filling(driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait.until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR)).click()
        active_element = wait.until(EC.visibility_of_element_located(TestLocators.ACTIVE_TAB_FILLING_LOCATOR))
        assert active_element.is_displayed()

    def test_tab_bun(driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Для "Булок" сначала переключаемся на "Начинки"
        wait.until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR)).click()
        wait.until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_BUN_LOCATOR)).click()
        active_element = wait.until(EC.visibility_of_element_located(TestLocators.ACTIVE_TAB_BUN_LOCATOR))
        assert active_element.is_displayed()
