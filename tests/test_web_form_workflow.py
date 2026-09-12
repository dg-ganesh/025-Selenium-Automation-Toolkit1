"""
Project : Selenium Automation Toolkit
Project ID : 025

Web Form Workflow Tests
"""

from src.core.browser_automation import BrowserAutomation
from src.core.web_form_page import WebFormPage
from src.core.web_form_workflow import WebFormWorkflow


def test_web_form_workflow(
    browser_automation: BrowserAutomation,
) -> None:
    """Verify that the Web Form workflow executes successfully."""
    page = WebFormPage(browser_automation)
    workflow = WebFormWorkflow(page)

    result = workflow.execute(
        text="Slice 3 workflow test"
    )

    assert result is True