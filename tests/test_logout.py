import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Локаторы
login_button = (By.XPATH, '//button[text()="Войти"]')
email_input = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
password_input = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
account_button = (By.XPATH, '//p[text()="Личный Кабинет"]')
logout_button = (By.XPATH, '//button[text()="Выход"]')

class TestAccount:
    @pytest.mark.parametrize("email, password", [
        ("testuser1@example.com", "ValidPass123"),
    ])
    def test_login_and_logout(driver, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 15)

    # Вводим логин и пароль
        wait.until(EC.visibility_of_element_located(email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(password_input)).send_keys(password)

    # Кнопка "Войти"
        wait.until(EC.element_to_be_clickable(login_button)).click()

    # Ждем, что кнопка Личный кабинет появится
        personal_account = wait.until(EC.visibility_of_element_located(account_button))

    # Переход в ЛК через JS
        driver.execute_script("arguments[0].click();", personal_account)

    # Небольшая пауза, чтобы меню успело открыться
        WebDriverWait(driver, 2)

    # Кликаем на "Выход" через JS
        logout_elem = wait.until(EC.presence_of_element_located(logout_button))
        driver.execute_script("arguments[0].click();", logout_elem)

    # Проверка: после выхода должна быть видна кнопка "Войти"
        assert wait.until(EC.visibility_of_element_located(login_button)).is_displayed()
