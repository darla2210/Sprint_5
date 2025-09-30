import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators

class TestLogout:
    @pytest.mark.parametrize("email, password", [
        ("testuser1@example.com", "ValidPass123"),
    ])
    def test_login_and_logout(driver, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 15)

        # Вводим логин и пароль
        wait.until(EC.visibility_of_element_located(TestLocators.email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.password_input)).send_keys(password)

        # Кнопка "Войти"
        wait.until(EC.element_to_be_clickable(TestLocators.login_button)).click()

        # Ждем, что кнопка Личный кабинет появится
        personal_account = wait.until(EC.visibility_of_element_located(TestLocators.account_button))

        # Переход в ЛК через JS
        driver.execute_script("arguments[0].click();", personal_account)

        # Кликаем на "Выход" через JS
        logout_elem = wait.until(EC.presence_of_element_located(TestLocators.logout_button))
        driver.execute_script("arguments[0].click();", logout_elem)

        # Проверка: после выхода должна быть видна кнопка "Войти"
        assert wait.until(EC.visibility_of_element_located(TestLocators.login_button)).is_displayed()
