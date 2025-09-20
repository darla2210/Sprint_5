import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Локаторы — только кортежи!
login_button = (By.XPATH, '//button[text()="Войти"]')
name_input = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
email_input = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
password_input = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
register_link = (By.XPATH, '//a[text()="Зарегистрироваться"]')
account_button = (By.XPATH, '//p[text()="Личный Кабинет"]')
register_button = (By.XPATH, '//button[text()="Зарегистрироваться"]')

@pytest.mark.parametrize("email, password, username", [
    ("testuser1@example.com", "ValidPass123", "testuser1"),
])
def test_successful_registration(driver, email, password, username):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    wait = WebDriverWait(driver, 20)

    # Переход на страницу регистрации
    wait.until(EC.element_to_be_clickable(register_link)).click()

    # Заполнение формы регистрации
    wait.until(EC.visibility_of_element_located(name_input)).send_keys(username)
    wait.until(EC.visibility_of_element_located(email_input)).send_keys(email)
    wait.until(EC.visibility_of_element_located(password_input)).send_keys(password)

    # Кнопка регистрации
    wait.until(EC.element_to_be_clickable(register_button)).click()

    # Проверяем, что после успешной регистрации видна кнопка «Личный Кабинет»
    assert wait.until(EC.visibility_of_element_located(account_button)).is_displayed()


def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    wait = WebDriverWait(driver, 20)

    # Переход на страницу регистрации
    wait.until(EC.element_to_be_clickable(register_link)).click()

    # Заполнение формы с некорректным паролем (например, слишком короткий)
    wait.until(EC.visibility_of_element_located(name_input)).send_keys("testuser2")
    wait.until(EC.visibility_of_element_located(email_input)).send_keys("testuser2@example.com")
    wait.until(EC.visibility_of_element_located(password_input)).send_keys("123")  # короткий пароль

    wait.until(EC.element_to_be_clickable(register_button)).click()

    # Проверяем, что есть сообщение об ошибке, содержащее слово «пароль»
    try:
        error = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "пароль")]')))
        assert error.is_displayed()
    except NoSuchElementException:
        pytest.fail("Ошибка пароля не отображается")
