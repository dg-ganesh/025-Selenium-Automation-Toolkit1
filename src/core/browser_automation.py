"""
Project : Selenium Automation Toolkit
Project ID : 025

Browser Automation Core
"""

from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.core.wait_utils import WaitUtils
from src.services.browser_service import BrowserService


class BrowserAutomation:
    """Provide reusable browser automation operations."""

    def __init__(self, browser_service: BrowserService) -> None:
        """Initialize browser automation with a browser service."""
        self._browser_service = browser_service
        self._wait_utils: Optional[WaitUtils] = None

    def _get_wait_utils(self) -> WaitUtils:
        """Return the wait utility for the active browser."""
        if self._wait_utils is None:
            self._wait_utils = WaitUtils(
                self._browser_service.get_driver()
            )

        return self._wait_utils

    def navigate(self, url: str) -> None:
        """Navigate the browser to the supplied URL."""
        self._browser_service.get_driver().get(url)

    def find_element(
        self,
        locator: tuple[By, str],
    ) -> WebElement:
        """Find an element after waiting for its presence."""
        return self._get_wait_utils().wait_for_presence(locator)

    def click(
        self,
        locator: tuple[By, str],
    ) -> None:
        """Click an element after waiting for it to be clickable."""
        element = self._get_wait_utils().wait_for_clickability(locator)
        element.click()

    def enter_text(
        self,
        locator: tuple[By, str],
        text: str,
    ) -> None:
        """Enter text into a visible element."""
        element = self._get_wait_utils().wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def get_text(
        self,
        locator: tuple[By, str],
    ) -> str:
        """Return the visible text of an element."""
        element = self._get_wait_utils().wait_for_visibility(locator)
        return element.text

    def verify_text(
        self,
        locator: tuple[By, str],
        expected_text: str,
    ) -> bool:
        """Verify that an element contains the expected text."""
        actual_text = self.get_text(locator)
        return actual_text == expected_text