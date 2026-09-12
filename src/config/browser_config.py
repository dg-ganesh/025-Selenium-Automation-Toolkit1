"""
Project : Selenium Automation Toolkit
Project ID : 025

Browser Configuration
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BrowserConfig:
    """Configuration settings for Selenium browser execution."""

    browser_name: str = "chrome"
    headless: bool = False
    start_maximized: bool = True