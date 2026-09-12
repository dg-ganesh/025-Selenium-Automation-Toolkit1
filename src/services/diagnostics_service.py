"""
Project : Selenium Automation Toolkit
Project ID : 025

Diagnostics Service
"""

from datetime import datetime
from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver

from src.config import LOGS_DIRECTORY


class DiagnosticsService:
    """Capture diagnostic information from Selenium execution."""

    def __init__(
        self,
        logs_directory: Path = LOGS_DIRECTORY,
    ) -> None:
        """Initialize the diagnostics service."""
        self._logs_directory = logs_directory
        self._logs_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def capture_screenshot(
        self,
        driver: WebDriver,
        name: str = "screenshot",
    ) -> Path:
        """
        Capture the current browser screen.

        Args:
            driver: Active Selenium WebDriver.
            name: Base name for the screenshot file.

        Returns:
            Path to the captured screenshot.
        """
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        screenshot_path = (
            self._logs_directory
            / f"{name}_{timestamp}.png"
        )

        driver.save_screenshot(str(screenshot_path))

        return screenshot_path