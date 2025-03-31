from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import *


class TestSwitchBlocksOnConstructor:
    # Проверка перехода из раздела "Булки" в раздел "Начинки" с авторизацией
    def test_navigate_to_fillings_from_buns_on_constructor_success(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        driver.find_element(*TestLocators.fillings_block_loc).click()
        assert driver.find_element(*TestLocators.button_selected_loc).text == 'Начинки'

    # Проверка перехода из раздела "Булки" в раздел "Соусы" с авторизацией
    def test_navigate_to_sauces_from_buns_on_constructor_success(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        driver.find_element(*TestLocators.sauces_block_loc).click()
        assert driver.find_element(*TestLocators.button_selected_loc).text == 'Соусы'

    # Проверка перехода из раздела "Соусы" в раздел "Булки" с авторизацией
    def test_navigate_to_buns_from_sauces_on_constructor_success(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order_loc))
        driver.find_element(*TestLocators.sauces_block_loc).click()
        driver.find_element(*TestLocators.buns_block_loc).click()
        assert driver.find_element(*TestLocators.button_selected_loc).text == 'Булки'

    # Проверка перехода из раздела "Соусы" в раздел "Начинки" без авторизации
    def test_navigate_to_fillings_from_sauces_on_constructor_success(self, driver):
        driver.get(TestLinks.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_in_main_loc))
        driver.find_element(*TestLocators.sauces_block_loc).click()
        driver.find_element(*TestLocators.fillings_block_loc).click()
        assert driver.find_element(*TestLocators.button_selected_loc).text == 'Начинки'

    # Проверка перехода из раздела "Начинки" в раздел "Соусы" без авторизации
    def test_navigate_to_sauces_from_fillings_on_constructor_success(self, driver):
        driver.get(TestLinks.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_in_main_loc))
        driver.find_element(*TestLocators.fillings_block_loc).click()
        driver.find_element(*TestLocators.sauces_block_loc).click()
        assert driver.find_element(*TestLocators.button_selected_loc).text == 'Соусы'

    # Проверка перехода из раздела "Начинки" в раздел "Булки" без авторизации
    def test_navigate_to_buns_from_fillings_on_constructor_success(self, driver):
        driver.get(TestLinks.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_in_main_loc))
        driver.find_element(*TestLocators.fillings_block_loc).click()
        driver.find_element(*TestLocators.buns_block_loc).click()
        assert driver.find_element(*TestLocators.button_selected_loc).text == 'Булки'
