"""
Project : Selenium Automation Toolkit
Project ID : 025

Selenium Wait Utilities
"""

from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config import DEFAULT_WAIT_SECONDS


class WaitUtils:
    """Provide reusable Selenium explicit-wait operations."""

    def __init__(
        self,
        driver: WebDriver,
        timeout: Optional[int] = None,
    ) -> None:
        """
        Initialize the wait utility.

        Args:
            driver: Active Selenium WebDriver instance.
            timeout: Optional wait timeout in seconds.
                Defaults to DEFAULT_WAIT_SECONDS.
        """
        self._driver = driver
        self._timeout = (
            timeout
            if timeout is not None
            else DEFAULT_WAIT_SECONDS
        )

    def wait_for_presence(
        self,
        locator: tuple[By, str],
    ) -> WebElement:
        """Wait until an element is present in the DOM."""
        return WebDriverWait(
            self._driver,
            self._timeout,
        ).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_visibility(
        self,
        locator: tuple[By, str],
    ) -> WebElement:
        """Wait until an element is visible."""
        return WebDriverWait(
            self._driver,
            self._timeout,
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickability(
        self,
        locator: tuple[By, str],
    ) -> WebElement:
        """Wait until an element is visible and clickable."""
        return WebDriverWait(
            self._driver,
            self._timeout,
        ).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url(self, url: str) -> bool:
        """Wait until the browser URL matches the expected URL."""
        return bool(
            WebDriverWait(
                self._driver,
                self._timeout,
            ).until(
                EC.url_to_be(url)
            )
        )