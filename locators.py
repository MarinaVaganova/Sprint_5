from selenium.webdriver.common.by import By


class TestLocators:
    # Регистрация
    # Поле "Имя"
    name_loc = By.XPATH, './/label[text() = "Имя"]/following-sibling::input'
    # Поле "Email"
    email_loc = By.XPATH, './/label[text() = "Email"]/following-sibling::input'
    # Поле "Пароль"
    password_loc = By.XPATH, './/input[@name = "Пароль"]'
    # Кнопка "Зарегистрироваться"
    button_submit_loc = By.XPATH, './/button[text() = "Зарегистрироваться"]'
    # Ошибка: пароль не прошел валидацию
    invalid_password_loc = By.XPATH, './/p[text() = "Некорректный пароль"]'
    # Кнопка "Войти" на форме регистрации
    button_login_in_reg_form_loc = By.XPATH, './/a[text() = "Войти"]'
    # Ошибка: попытка повторной регистрации пользователя
    re_registration_loc = By.XPATH, './/p[text() = "Такой пользователь уже существует"]'

    # Аутентификация
    # Поле "Email"
    email_auth_loc = By.XPATH, './/label[text() = "Email"]/following-sibling::input'
    # Поле "Пароль"
    password_auth_loc = By.XPATH, './/input[@name = "Пароль"]'
    # Кнопка "Войти"
    button_login_auth_loc = By.XPATH, './/button[text() = "Войти"]'
    # Кнопка "Зарегистрироваться"
    button_reg_loc = By.XPATH, './/a[text() = "Зарегистрироваться"]'

    # Восстановление пароля
    # Кнопка "Восстановить пароль"
    button_forgot_password_loc = By.XPATH, './/a[text() = "Восстановить пароль"]'
    # Кнопка "Войти" на форме восстановления пароля
    button_login_recovery_form_loc = By.XPATH, './/a[text() = "Войти"]'

    # Личный кабинет
    # Раздел "Профиль"
    profile_loc = By.XPATH, './/a[@href = "/account/profile"]'
    # Раздел "История заказов"
    order_history_loc = By.XPATH, './/a[@href = "/account/order-history"]'
    # Кнопка "Выход"
    button_logout_loc = By.XPATH, './/button[@type = "button" and text()="Выход"]'

    # Главная страница
    # Кнопка "Войти в аккаунт"
    button_login_in_main_loc = By.XPATH, '//button[text()="Войти в аккаунт"]'
    # Кнопка "Личный кабинет"
    button_personal_account_loc = By.XPATH, '//p[text() = "Личный Кабинет"]'
    # Кнопка "Оформить заказ"
    button_make_the_order_loc = By.XPATH, '//button[text() = "Оформить заказ"]'
    # Кнопка "Конструктор"
    header_of_page_constructor_loc = By.XPATH, '//p[text() = "Конструктор"]'
    # Селектор, отмечающий выбранный раздел конструктора, как активный
    button_selected_loc = By.XPATH, '//div[@class = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'
    # Заголовок раздела "Булки" в меню конструктора
    buns_block_loc = By.XPATH, '//span[text() = "Булки"]'
    # Заголовок раздела "Соусы" в меню конструктора
    sauces_block_loc = By.XPATH, '//span[text() = "Соусы"]'
    # Заголовок раздела "Начинки" в меню конструктора
    fillings_block_loc = By.XPATH, '//span[text() = "Начинки"]'
    # Логотип в шапке сайта
    logo_loc = By.XPATH, '//div[@class = "AppHeader_header__logo__2D0X2"]'