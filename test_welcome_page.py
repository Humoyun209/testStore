from pages.welcome_page import WelcomePage


def test_check_login_and_register_links(browser):
    link = 'http://80.249.147.135/'
    page = WelcomePage(browser, link)
    page.open()
    page.should_be_login_link()
    page.should_be_login_register()


def test_go_to_login_from_welcome_page(browser):
    link = 'http://80.249.147.135/'
    page = WelcomePage(browser, link)
    page.open()
    page.go_to_register_on_mobile()
    page.shoule_be_register_form()