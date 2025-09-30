import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random
from locators import TestLocators
from utils import generate_email, generate_password



class TestRegister:
    @pytest.mark.parametrize("password, username", [
        ("ValidPass123", "testuser1"),
    ])
    def test_successful_registration(driver, password, username):
        email = generate_email()  # <- здесь теперь рандомный email

        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 20)

        # Переход на страницу регистрации
        wait.until(EC.element_to_be_clickable(TestLocators.register_link)).click()

        # Заполнение формы регистрации
        wait.until(EC.visibility_of_element_located(TestLocators.name_input)).send_keys(username)
        wait.until(EC.visibility_of_element_located(TestLocators.email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.password_input)).send_keys(password)

        # Кнопка регистрации
        wait.until(EC.element_to_be_clickable(TestLocators.register_button)).click()

        # Проверяем, что после успешной регистрации видна кнопка «Личный Кабинет»
        assert wait.until(EC.visibility_of_element_located(TestLocators.account_button)).is_displayed()


    def test_registration_with_invalid_password(driver):
        email = generate_email()  # <- рандомный email для теста с неправильным паролем

        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 20)

        # Переход на страницу регистрации
        wait.until(EC.element_to_be_clickable(TestLocators.register_link)).click()

        # Заполнение формы с некорректным паролем (например, слишком короткий)
        wait.until(EC.visibility_of_element_located(TestLocators.name_input)).send_keys("testuser2")
        wait.until(EC.visibility_of_element_located(TestLocators.email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.password_input)).send_keys("123")  # короткий пароль

        wait.until(EC.element_to_be_clickable(TestLocators.register_button)).click()

    # Проверяем, что есть сообщение об ошибке, содержащее слово «пароль»
        error = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "пароль")]')))
        assert error.is_displayed()

