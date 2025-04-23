from pages.form_page import FormPage
import pytest

@pytest.mark.ui
def test_form_submission(browser):
    form_page = FormPage(browser)
    form_page.open()
    form_page.fill_out_form("John", "Doe", "john.doe@example.com")
    assert form_page.is_submission_successful()
