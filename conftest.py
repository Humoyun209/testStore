import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    print('\n open browser....')
    yield browser
    print('\n quit browser....')
    browser.quit()