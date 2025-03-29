# Sprint_5

### Описание проекта
Автотесты для сервиса Stellar Burgers. Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

### Структура проекта
1. Тесты: директория tests
2. Фикстуры: conftest.py
3. Статические данные: data.py
4. Генерация логина и пароля: generator.py
5. Локаторы: locators.py

### Реализованные проверки
##### 1. Регистрация: ```test_registration.py```  
Успешная регистрация: test_successful_registration  
Ошибка для некорректного пароля: test_registration_invalid_password_failed_submit, test_registration_invalid_password_error_message  
Ошибка при попытке повторной регистрации: test_registration_user_re_registration_error_message  
##### 2. Вход: ```test_authentication.py```  
Вход по кнопке «Войти в аккаунт» на главной: test_authentication_by_button_login_in_main_page_success  
Вход через кнопку «Личный кабинет»: test_authentication_by_button_personal_account_in_main_page_success  
Вход через кнопку в форме регистрации: test_authentication_by_button_login_in_registration_form_success  
Вход через кнопку в форме восстановления пароля: test_authentication_by_button_forgot_password_in_auth_form_success  
##### 3. Переход в личный кабинет: ```test_navigate_to_personal_account.py```  
Переход по клику на «Личный кабинет»: test_navigate_to_personal_account_success  
##### 4. Переход из личного кабинета в конструктор: ```test_navigate_to_constructor.py```
Переход по клику на «Конструктор»: test_navigate_from_personal_account_to_constructor_by_header_success  
Переход по клику на логотип Stellar Burgers: test_navigate_from_personal_account_by_logo_success  
##### 5. Выход из аккаунта: ```test_logout.py```
Выход по кнопке «Выйти» в личном кабинете: test_logout_of_personal_account_success  
##### 6. Раздел «Конструктор» ```test_switch_blocks_on_constructor.py```
Переходы к разделам «Булки», «Соусы», «Начинки»:  
"Булки" --> "Начинки" с авторизацией: test_navigate_to_fillings_from_buns_on_constructor_success  
"Булки" --> "Соусы" с авторизацией: test_navigate_to_sauces_from_buns_on_constructor_success  
"Соусы" --> "Булки" с авторизацией: test_navigate_to_buns_from_sauces_on_constructor_success  
"Соусы" --> "Начинки" без авторизации: test_navigate_to_fillings_from_sauces_on_constructor_success  
"Начинки" --> "Соусы" без авторизации: test_navigate_to_sauces_from_fillings_on_constructor_success  
"Начинки" --> "Булки" без авторизации: test_navigate_to_buns_from_fillings_on_constructor_success  
