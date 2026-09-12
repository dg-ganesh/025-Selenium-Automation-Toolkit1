"""
Project : Selenium Automation Toolkit
Project ID : 025

Web Form Workflow
"""

from src.config import TEST_URL
from src.core.web_form_page import WebFormPage


class WebFormWorkflow:
    """Execute the Web Form automation workflow."""

    EXPECTED_HEADING = "Web form"
    EXPECTED_RESULT_MESSAGE = "Received!"

    def __init__(self, page: WebFormPage) -> None:
        """Initialize the workflow with a Web Form page object."""
        self._page = page

    def execute(self, text: str) -> bool:
        """Execute the Web Form workflow and verify the result."""

        self._page.open()

        if not self._page.verify_heading(
            self.EXPECTED_HEADING
        ):
            return False

        self._page.enter_text(text)
        self._page.submit()

        return self._page.verify_result_message(
            self.EXPECTED_RESULT_MESSAGE
        )