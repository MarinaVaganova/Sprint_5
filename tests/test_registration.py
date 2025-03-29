import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from data import *
from generator import TestGenerator
from conftest import driver


class TestRegistration:
    # Проверка успешной регистрации
    def test_successful_registration(self, driver):
        test_email = TestGenerator.generate_email()
        test_password = TestGenerator.generate_password()
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_login_in_main_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.button_reg_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_loc))
        driver.find_element(*TestLocators.name_loc).send_keys(UserTestData.USERNAME)
        driver.find_element(*TestLocators.email_loc).send_keys(test_email)
        driver.find_element(*TestLocators.password_loc).send_keys(test_password)
        driver.find_element(*TestLocators.button_submit_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_auth_loc))
        assert driver.find_element(*TestLocators.button_reg_loc).is_displayed()

    # Проверка регистрации с некорректным паролем
    @pytest.mark.parametrize('invalid_password', ['G@hjk','прль1','0',''])
    def test_registration_invalid_password_failed_submit(self, driver, invalid_password):
        test_email = TestGenerator.generate_email()
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_login_in_main_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.button_reg_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_loc))
        driver.find_element(*TestLocators.name_loc).send_keys(UserTestData.USERNAME)
        driver.find_element(*TestLocators.email_loc).send_keys(test_email)
        driver.find_element(*TestLocators.password_loc).send_keys(invalid_password)
        driver.find_element(*TestLocators.button_submit_loc).click()
        assert driver.find_element(*TestLocators.button_submit_loc).is_displayed()

    # Проверка появления сообщения об ошибке при регистрации с некорректным паролем
    @pytest.mark.parametrize('invalid_password', ['G@hjk', 'прль1', '0'])
    def test_registration_invalid_password_error_message(self, driver, invalid_password):
        test_email = TestGenerator.generate_email()
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.button_reg_loc).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_loc))
        driver.find_element(*TestLocators.name_loc).send_keys(UserTestData.USERNAME)
        driver.find_element(*TestLocators.email_loc).send_keys(test_email)
        driver.find_element(*TestLocators.password_loc).send_keys(invalid_password)
        driver.find_element(*TestLocators.button_submit_loc).click()
        assert driver.find_element(*TestLocators.invalid_password_loc).text == 'Некорректный пароль'

    # Проверка появления сообщения об ошибке при повторной регистрации пользователя
    def test_registration_user_re_registration_error_message(self, driver):
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.button_reg_loc).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_loc))
        driver.find_element(*TestLocators.name_loc).send_keys(UserTestData.USERNAME)
        driver.find_element(*TestLocators.email_loc).send_keys(UserTestData.EMAIL)
        driver.find_element(*TestLocators.password_loc).send_keys(UserTestData.PASSWORD)
        driver.find_element(*TestLocators.button_submit_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.re_registration_loc))
        assert driver.find_element(*TestLocators.re_registration_loc).text == 'Такой пользователь уже существует'
