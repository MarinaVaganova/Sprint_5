import pytest
from selenium import webdriver

from data import *
from locators import TestLocators


# Фикстура веб-драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура для авторизации ранее зарегистрированного пользователя
@pytest.fixture(scope = 'function')
def login(driver):
    driver.get(TestLinks.URL)
    driver.find_element(*TestLocators.button_login_in_main_loc).click()
    driver.find_element(*TestLocators.email_auth_loc).send_keys(UserTestData.EMAIL)
    driver.find_element(*TestLocators.password_auth_loc).send_keys(UserTestData.PASSWORD)
    driver.find_element(*TestLocators.button_login_auth_loc).click()