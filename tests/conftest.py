"""
Project : Selenium Automation Toolkit
Project ID : 025

Pytest Fixtures
"""

from typing import Generator

import pytest

from src.core.browser_automation import BrowserAutomation
from src.services.browser_service import BrowserService
from src.services.diagnostics_service import DiagnosticsService


@pytest.fixture
def browser_automation(
    request: pytest.FixtureRequest,
) -> Generator[BrowserAutomation, None, None]:
    """Provide a started browser automation instance."""
    browser_service = BrowserService()
    browser_service.start()

    automation = BrowserAutomation(browser_service)

    request.node.browser_service = browser_service

    try:
        yield automation
    finally:
        browser_service.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item,
    call: pytest.CallInfo[None],
) -> Generator[None, None, None]:
    """Capture a screenshot when a browser test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    browser_service = getattr(
        item,
        "browser_service",
        None,
    )

    if browser_service is None:
        return

    driver = browser_service.driver

    if driver is None:
        return

    diagnostics_service = DiagnosticsService()

    screenshot_path = diagnostics_service.capture_screenshot(
        driver,
        name=item.name,
    )

    print(
        f"\nFailure screenshot: {screenshot_path}"
    )