import time

import pytest


def test_open_main_page(browser):
    browser.get('http://80.249.147.135/')
    time.sleep(10)