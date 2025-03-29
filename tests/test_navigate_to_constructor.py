from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import *


class TestNavigateToConstructor:
    # Проверка перехода по клику на "Конструктор" из Личного кабинета
    def test_navigate_from_personal_account_to_constructor_by_header_success(self, driver, login):
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.profile_loc))
        driver.find_element(*TestLocators.header_of_page_constructor_loc).click()
        assert driver.current_url == TestLinks.URL

    # Проверка перехода по клику на логотип Stellar Burgers из Личного кабинета
    def test_navigate_from_personal_account_by_logo_success(self, driver, login):
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.profile_loc))
        driver.find_element(*TestLocators.logo_loc).click()
        assert driver.current_url == TestLinks.URL
