"""
Project : Selenium Automation Toolkit
Project ID : 025

Web Form Page Object
"""

from src.config import TEST_URL
from src.core.base_page import BasePage


class WebFormPage(BasePage):
    """Represent the Selenium Web Form page."""

    PAGE_HEADING = ("tag name", "h1")
    TEXT_INPUT = ("name", "my-text")
    SUBMIT_BUTTON = ("css selector", "button")
    RESULT_MESSAGE = ("id", "message")

    def open(self) -> None:
        """Open the Web Form page."""
        self.navigate(TEST_URL)

    def get_heading(self) -> str:
        """Return the Web Form page heading."""
        return self.get_text(self.PAGE_HEADING)

    def verify_heading(self, expected_heading: str) -> bool:
        """Verify the Web Form page heading."""
        return self.verify_text(
            self.PAGE_HEADING,
            expected_heading,
        )

    def enter_text(self, text: str) -> None:
        """Enter text into the Web Form input field."""
        super().enter_text(
            self.TEXT_INPUT,
            text,
        )

    def submit(self) -> None:
        """Submit the Web Form."""
        self.click(self.SUBMIT_BUTTON)

    def get_result_message(self) -> str:
        """Return the message displayed after form submission."""
        return self.get_text(self.RESULT_MESSAGE)

    def verify_result_message(
        self,
        expected_message: str,
    ) -> bool:
        """Verify the message displayed after form submission."""
        return self.verify_text(
            self.RESULT_MESSAGE,
            expected_message,
        )