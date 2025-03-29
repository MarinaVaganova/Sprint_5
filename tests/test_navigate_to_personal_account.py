from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import *


class TestNavigateToPersonalAccount:
    # Проверка перехода по клику на "Личный кабинет"
    def test_navigate_to_personal_account_success(self, driver, login):
        driver.find_element(*TestLocators.button_personal_account_loc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.profile_loc))
        assert driver.find_element(*TestLocators.order_history_loc).is_displayed()
