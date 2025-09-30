import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestLogin:

    @pytest.mark.parametrize("email, password", [("testuser1@example.com", "ValidPass123")])
    def test_login_main_page(driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 10)

        # Вход по кнопке «Войти в аккаунт» на главной
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_MAIN_PAGE_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        personal_account_button = wait.until(
            EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        )
        assert personal_account_button.is_displayed()


    @pytest.mark.parametrize("email, password", [("testuser1@example.com", "ValidPass123")])
    def test_login_personal_account_button(driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 10)

        # Вход через кнопку «Личный кабинет» на главной
        wait.until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        account_button = wait.until(
            EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        )
        assert account_button.is_displayed()


    @pytest.mark.parametrize("email, password", [("testuser1@example.com", "ValidPass123")])
    def test_login_from_registration_form(driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        wait = WebDriverWait(driver, 10)

        # Вход через кнопку «Войти» на форме регистрации
        wait.until(EC.element_to_be_clickable(TestLocators.register_link)).click()
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        account_button = wait.until(
            EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        )
        assert account_button.is_displayed()


    @pytest.mark.parametrize("email, password", [("testuser1@example.com", "ValidPass123")])
    def test_login_from_password_recovery(driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        wait = WebDriverWait(driver, 10)

        # Вход через кнопку «Войти» на форме восстановления пароля
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
        wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        account_button = wait.until(
            EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        )
        assert account_button.is_displayed()
