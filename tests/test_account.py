import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from locators import TestLocators
from utils import generate_email, generate_password

register_link = (By.XPATH, '//a[text()="Зарегистрироваться"]')
name_input = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
email_input = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
password_input = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
register_button = (By.XPATH, '//button[text()="Зарегистрироваться"]')
account_button = (By.XPATH, '//p[text()="Личный Кабинет"]')

@pytest.mark.parametrize("username", ["testuser"])
def test_register_login_and_go_to_personal_account(driver, username):
    email = generate_email()
    password = generate_password()

    wait = WebDriverWait(driver, 15)

    driver.get("https://stellarburgers.nomoreparties.site/login")

    wait.until(EC.element_to_be_clickable(register_link)).click()

    wait.until(EC.visibility_of_element_located(name_input)).send_keys(username)
    wait.until(EC.visibility_of_element_located(email_input)).send_keys(email)
    wait.until(EC.visibility_of_element_located(password_input)).send_keys(password)

    wait.until(EC.element_to_be_clickable(register_button)).click()

    wait.until(EC.visibility_of_element_located(account_button))

   # Явно переходим на страницу логина
    driver.get("https://stellarburgers.nomoreparties.site/login")

   # Вводим email и пароль
    wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
    wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)

# Нажимаем кнопку "Войти"
    wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_LOCATOR)).click()

    time.sleep(5)

    wait.until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()

    time.sleep(10)

    assert "account" in driver.current_url
