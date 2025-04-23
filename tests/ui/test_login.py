from pages.login_page import LoginPage
import pytest

@pytest.mark.ui
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("admin", "password123")
    assert login_page.is_logged_in()

@pytest.mark.ui
def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("wrong_user", "wrong_password")
    assert login_page.is_error_displayed()
