import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from locators import TestLocators
from utils import generate_email, generate_password

class TestAccount:

    @pytest.mark.parametrize("username", ["testuser"])
    def test_register_login_and_go_to_personal_account(self, driver, username):
        email = generate_email()
        password = generate_password()

        wait = WebDriverWait(driver, 15)

        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Переход на страницу регистрации
        wait.until(EC.element_to_be_clickable(TestLocators.register_link)).click()

        # Заполнение формы регистрации
        wait.until(EC.visibility_of_element_located(TestLocators.name_input)).send_keys(username)
        wait.until(EC.visibility_of_element_located(TestLocators.email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.password_input)).send_keys(password)

        # Клик по кнопке "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(TestLocators.register_button)).click()

        # Проверяем, что появилась кнопка "Личный кабинет"
        wait.until(EC.visibility_of_element_located(TestLocators.account_button))

        # Явно переходим на страницу логина
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Вводим email и пароль
        wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)

        # Нажимаем кнопку "Войти"
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_LOCATOR)).click()

        # Переходим в ЛК
        wait.until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()

        assert "account" in driver.current_url

    def test_go_to_constructor_from_account(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.nomoreparties.site/account")

        # Кликаем на кнопку "Конструктор"
        wait.until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON_LOCATOR)).click()

        # Проверяем, что кнопка "Оформить заказ" видна
        assert wait.until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON)).is_displayed()

    def test_go_to_constructor_from_logo(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.nomoreparties.site/account")

        # Кликаем на логотип Stellar Burgers
        wait.until(EC.element_to_be_clickable(TestLocators.LOGO_LOCATOR)).click()

        # Проверяем, что кнопка "Оформить заказ" видна
        assert wait.until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON)).is_displayed()
