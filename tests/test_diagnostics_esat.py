"""
Project : Selenium Automation Toolkit
Project ID : 025

Final ESAT - Failure Diagnostics
"""

from src.core.browser_automation import BrowserAutomation


def test_failure_diagnostics_esat(
    browser_automation: BrowserAutomation,
) -> None:
    """Verify that a browser screenshot is captured on failure."""

    browser_automation.navigate(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )

    assert False, "Intentional ESAT failure for diagnostics validation"
    