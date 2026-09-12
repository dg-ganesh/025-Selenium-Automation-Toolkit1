"""
Project : Selenium Automation Toolkit
Project ID : 025

Base Page Object
"""

from src.core.browser_automation import BrowserAutomation


class BasePage:
    """Provide the common foundation for Selenium Page Objects."""

    def __init__(self, automation: BrowserAutomation) -> None:
        """Initialize the page object with browser automation."""
        self._automation = automation

    @property
    def automation(self) -> BrowserAutomation:
        """Return the browser automation interface."""
        return self._automation

    def navigate(self, url: str) -> None:
        """Navigate to the specified URL."""
        self._automation.navigate(url)

    def click(self, locator: tuple[str, str]) -> None:
        """Click an element identified by the locator."""
        self._automation.click(locator)

    def enter_text(
        self,
        locator: tuple[str, str],
        text: str,
    ) -> None:
        """Enter text into an element identified by the locator."""
        self._automation.enter_text(locator, text)

    def get_text(
        self,
        locator: tuple[str, str],
    ) -> str:
        """Return text from an element identified by the locator."""
        return self._automation.get_text(locator)

    def verify_text(
        self,
        locator: tuple[str, str],
        expected_text: str,
    ) -> bool:
        """Verify that an element contains the expected text."""
        return self._automation.verify_text(
            locator,
            expected_text,
        )

    def verify_title(self, expected_title: str) -> bool:
        """Verify the current page title."""
        return self._automation.verify_title(expected_title)

    def current_url(self) -> str:
        """Return the current browser URL."""
        return self._automation.current_url()