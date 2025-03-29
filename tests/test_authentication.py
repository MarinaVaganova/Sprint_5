from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import driver
from data import *


class TestAuthentication:
    # Вход через кнопку "Войти в аккаунт" на главной
    def test_authentication_by_button_login_in_main_page_success(self, driver):
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_login_in_main_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.email_auth_loc).send_keys(UserTestData.EMAIL)
        driver.find_element(*TestLocators.password_auth_loc).send_keys(UserTestData.PASSWORD)
        driver.find_element(*TestLocators.button_login_auth_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        assert driver.find_element(*TestLocators.button_make_the_order_loc).is_displayed()

    # Вход через кнопку "Личный кабинет"
    def test_authentication_by_button_personal_account_in_main_page_success(self, driver):
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.email_auth_loc).send_keys(UserTestData.EMAIL)
        driver.find_element(*TestLocators.password_auth_loc).send_keys(UserTestData.PASSWORD)
        driver.find_element(*TestLocators.button_login_auth_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        assert driver.find_element(*TestLocators.button_make_the_order_loc).is_displayed()

    # Вход через кнопку в форме регистрации
    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_login_in_main_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.button_reg_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_loc))
        driver.find_element(*TestLocators.button_login_in_reg_form_loc).click()
        driver.find_element(*TestLocators.email_auth_loc).send_keys(UserTestData.EMAIL)
        driver.find_element(*TestLocators.password_auth_loc).send_keys(UserTestData.PASSWORD)
        driver.find_element(*TestLocators.button_login_auth_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        assert driver.find_element(*TestLocators.button_make_the_order_loc).is_displayed()

    # Вход через кнопку в форме восстановления пароля
    def test_authentication_by_button_forgot_password_in_auth_form_success(self, driver):
        driver.get(TestLinks.URL)
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.button_forgot_password_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_recovery_form_loc))
        driver.find_element(*TestLocators.button_login_recovery_form_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_reg_loc))
        driver.find_element(*TestLocators.email_auth_loc).send_keys(UserTestData.EMAIL)
        driver.find_element(*TestLocators.password_auth_loc).send_keys(UserTestData.PASSWORD)
        driver.find_element(*TestLocators.button_login_auth_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        assert driver.find_element(*TestLocators.button_make_the_order_loc).is_displayed()
        