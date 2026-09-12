"""
Project : Selenium Automation Toolkit
Project ID : 025

Browser Service
"""

from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from src.config import BROWSER_CONFIG


class BrowserService:
    """Manage the Selenium WebDriver lifecycle."""

    def __init__(self) -> None:
        self._driver: Optional[WebDriver] = None

    def start(self) -> WebDriver:
        """
        Start the configured browser and return the WebDriver instance.

        Raises:
            ValueError: If the configured browser is unsupported.
            RuntimeError: If the browser cannot be started.
        """
        if self._driver is not None:
            return self._driver

        try:
            if BROWSER_CONFIG.browser_name.lower() == "chrome":
                options = Options()

                if BROWSER_CONFIG.headless:
                    options.add_argument("--headless=new")

                if BROWSER_CONFIG.start_maximized:
                    options.add_argument("--start-maximized")

                self._driver = webdriver.Chrome(options=options)

            else:
                raise ValueError(
                    f"Unsupported browser configured: "
                    f"{BROWSER_CONFIG.browser_name}"
                )

            return self._driver

        except Exception as exc:
            self._driver = None
            raise RuntimeError(
                f"Unable to start browser "
                f"'{BROWSER_CONFIG.browser_name}': {exc}"
            ) from exc

    def get_driver(self) -> WebDriver:
        """
        Return the active WebDriver instance.

        Raises:
            RuntimeError: If the browser has not been started.
        """
        if self._driver is None:
            raise RuntimeError("Browser has not been started.")

        return self._driver

    def close(self) -> None:
        """Close the active browser session and release the WebDriver."""
        if self._driver is not None:
            try:
                self._driver.quit()
            finally:
                self._driver = None

    @property
    def driver(self) -> Optional[WebDriver]:
        """Return the active WebDriver, or None if no browser is running."""
        return self._driver