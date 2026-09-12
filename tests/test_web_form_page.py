"""
Project : Selenium Automation Toolkit
Project ID : 025

Web Form Page Tests
"""

from src.core.browser_automation import BrowserAutomation
from src.core.web_form_page import WebFormPage


def test_web_form_page_heading(
    browser_automation: BrowserAutomation,
) -> None:
    """Verify that the Web Form page opens correctly."""
    page = WebFormPage(browser_automation)

    page.open()

    assert page.verify_heading("Web form") is True


def test_web_form_page_submission(
    browser_automation: BrowserAutomation,
) -> None:
    """Verify that the Web Form can be submitted successfully."""
    page = WebFormPage(browser_automation)

    page.open()
    page.enter_text("Slice 3 page test")
    page.submit()

    assert page.verify_result_message("Received!") is True