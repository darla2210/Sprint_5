import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators


@pytest.mark.parametrize("email, password", [
    ("testuser1@example.com", "ValidPass123"),
])
def test_login_main_page(driver, email, password):
    driver.get('https://stellarburgers.nomoreparties.site/')
    wait = WebDriverWait(driver, 10)

    # Кликаем "Войти в аккаунт"
    wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_MAIN_PAGE_BUTTON)).click()

    # Вводим email и пароль
    wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
    wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)

    # Жмём кнопку "Войти"
    wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

    # Проверяем, что появилась кнопка "Личный кабинет" (успешный вход)
    personal_account_button = wait.until(
        EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
    )

    # Явная проверка, что элемент действительно отображается
    assert personal_account_button.is_displayed()
