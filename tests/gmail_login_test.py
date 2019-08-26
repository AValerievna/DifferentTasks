# encoding=utf-8
import pytest

from hamcrest import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# на проекте, на котором я работаю, принято выносить "хардкодные" данные в константы
PATH_DATA = "http://www.gmail.com"
TIMEOUT_DATA = 60


class TestFile(object):

    @pytest.mark.parametrize("login_data, passw", [
        ("<<valid_login>>", "<<valid_passw>>"),
        pytest.param("<<valid_login>>", "invalid_passw",
                     marks=pytest.mark.xfail(reason="invalid args", strict=True)),
        pytest.param("invalid_login", "some_passw",
                     marks=pytest.mark.xfail(reason="invalid args", strict=True)),
    ])
    def test_gmail_login(self, driver, login_data, passw):
        """Тестовый сценарий авторизации в gmail.com.

        Args:
            driver: Фикстура работы с браузером.
            login_data: Данный логина.
            passw: Данные пароля.

        """
        driver.get(PATH_DATA)

        WebDriverWait(driver, TIMEOUT_DATA).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
        input_email = driver.find_element_by_xpath("//input[@type='email']")
        input_email.send_keys(login_data)

        email_next_btn = driver.find_element_by_xpath("//div[@id='identifierNext']")
        email_next_btn.click()

        WebDriverWait(driver, TIMEOUT_DATA).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
        input_passw = driver.find_element_by_xpath("//input[@type='password']")

        input_passw.send_keys(passw)
        passw_next_btn = driver.find_element_by_xpath("//div[@id='passwordNext']")
        passw_next_btn.click()
        WebDriverWait(driver, TIMEOUT_DATA).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Inbox')]")))
        assert_that(driver.find_element_by_xpath("//a[contains(text(),'Inbox')]"))


