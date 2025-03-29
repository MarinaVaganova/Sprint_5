from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import *


class TestLogout:
    # Проверка выхода по кнопке "Выйти" в Личном кабинете
    def test_logout_of_personal_account_success(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.profile_loc))
        driver.find_element(*TestLocators.button_logout_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_auth_loc))
        assert driver.find_element(*TestLocators.button_login_auth_loc).is_displayed()
