import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

@pytest.mark.parametrize("tab_button, active_tab", [
    (TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR, TestLocators.ACTIVE_TAB_SAUCE_LOCATOR),
    (TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR, TestLocators.ACTIVE_TAB_FILLING_LOCATOR),
    (TestLocators.CONSTRUCTOR_TAB_BUN_LOCATOR, TestLocators.ACTIVE_TAB_BUN_LOCATOR),
])
def test_constructor_tabs(driver, tab_button, active_tab):
    wait = WebDriverWait(driver, 15)
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Если надо кликнуть на «Булки», сначала переключаемся на «Начинки» чтобы можно было потом переключиться на «Булки»
    if tab_button == TestLocators.CONSTRUCTOR_TAB_BUN_LOCATOR:
        wait.until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR)).click()

    wait.until(EC.element_to_be_clickable(tab_button)).click()

    active_element = wait.until(EC.visibility_of_element_located(active_tab))
    assert active_element.is_displayed()
