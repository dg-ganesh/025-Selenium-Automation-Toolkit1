"""
Project : Selenium Automation Toolkit
Project ID : 025

Application Configuration
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BrowserConfig:
    """Configuration settings for Selenium browser execution."""

    browser_name: str = "chrome"
    headless: bool = False
    start_maximized: bool = True


# Application information
APPLICATION_NAME = "Selenium Automation Toolkit"
APPLICATION_VERSION = "1.0.0"
PROJECT_ID = "025"


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOGS_DIRECTORY = PROJECT_ROOT / "logs"
EXECUTION_REPORT_PATH = LOGS_DIRECTORY / "execution_report.txt"


# Selenium test configuration
TEST_URL = "https://www.selenium.dev/selenium/web/web-form.html"


# Browser configuration
BROWSER_CONFIG = BrowserConfig(
    browser_name="chrome",
    headless=False,
    start_maximized=True,
)


# Selenium behaviour
DEFAULT_WAIT_SECONDS = 10

# Development / visual execution
VISUAL_DELAY_SECONDS = 0