from selenium.webdriver.common.by import By


class TestLocators:
    # Локаторы полей ввода логина и пароля (подарок от наставника)
    EMAIL_LOCATOR = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    email_input = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    PASSWORD_LOCATOR = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
    password_input = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    
    # поле ввода имени в форме регистрации
    NAME_LOCATOR = (By.XPATH, ".//*[text()='Имя']/following-sibling::input")
    name_input = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    


    # Кнопка "Войти в аккаунт" на главной странице и "Войти" в ЛК
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "button_button_type_primary")]')
    login_button = (By.XPATH, '//button[text()="Войти"]')
    1. #локатор кнопки "Войти в аккаунт"
    LOGIN_MAIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # кнопка войти после кнопки войти в акк
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    # ссылка "Войти" на страницах регистрации и восстановления пароля
    LOGIN_LINK_LOCATOR = (By.XPATH, '//*[contains(@class, "Auth_link")]')

    # кнопка "Зарегистрироваться" в форме регистрации
    REGISTER_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "button_button_type_primary")]')
    register_link = (By.XPATH, '//a[text()="Зарегистрироваться"]')
    register_button = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    # кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    account_button = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(), 'Конструктор')]")

    # кнопка "Выход" в ЛК
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(@class, 'Account_button')]")

    # логотип Stellar Burgers в header
    LOGO_LOCATOR = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")

    # Локаторы для вкладок конструктора
    CONSTRUCTOR_TAB_BUN_LOCATOR = (By.XPATH, "*//span[contains(text(), 'Булки')]")
    CONSTRUCTOR_TAB_SAUCE_LOCATOR = (By.XPATH, "*//span[contains(text(), 'Соусы')]")
    CONSTRUCTOR_TAB_FILLING_LOCATOR = (By.XPATH, "*//span[contains(text(), 'Начинки')]")

    # Локаторы для активных вкладок
    ACTIVE_TAB_BUN_LOCATOR = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Булки']]")
    ACTIVE_TAB_SAUCE_LOCATOR = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Соусы']]")
    ACTIVE_TAB_FILLING_LOCATOR = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Начинки']]")

    # Локатор ошибки неправильного логина при регистрации
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, ".input__error.text_type_main-default")

    WRONG_PASS_MESSAGE_LOCATOR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

    # локато "оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')