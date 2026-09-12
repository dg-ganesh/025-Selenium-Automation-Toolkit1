"""
Project : Selenium Automation Toolkit
Project ID : 025

Web Form Validation Tests
"""

import pytest

from src.core.browser_automation import BrowserAutomation
from src.core.web_form_page import WebFormPage
from src.core.web_form_workflow import WebFormWorkflow


@pytest.mark.parametrize(
    "test_input",
    [
        "Slice 3 validation test",
        "Selenium Automation Toolkit",
        "Python Test Automation",
    ],
)
def test_web_form_workflow_with_valid_input(
    browser_automation: BrowserAutomation,
    test_input: str,
) -> None:
    """Verify the workflow succeeds with different valid inputs."""
    page = WebFormPage(browser_automation)
    workflow = WebFormWorkflow(page)

    result = workflow.execute(
        text=test_input
    )

    assert result is True