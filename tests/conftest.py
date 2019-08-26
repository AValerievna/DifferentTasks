# encoding=utf8
import pytest

from selenium import webdriver

# на проекте, на котором я работаю, принято выносить "хардкодные" данные в константы
CHROME_DRIVER_PATH = ".\\chromedriver.exe"


@pytest.fixture(scope='function')
def driver():
    u"""Фикстура работы с браузером"""
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()