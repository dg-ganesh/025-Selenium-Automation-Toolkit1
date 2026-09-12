"""
Project : Selenium Automation Toolkit
Project ID : 025

Logging Service
"""

from datetime import datetime
from pathlib import Path
from time import perf_counter
from typing import Optional

from src.config import (
    APPLICATION_VERSION,
    EXECUTION_REPORT_PATH,
    LOGS_DIRECTORY,
)


class LoggingService:
    """Manage runtime logging and execution reporting."""

    def __init__(self) -> None:
        self._start_time: Optional[float] = None
        self._execution_start: Optional[datetime] = None
        self._last_checkpoint: Optional[str] = None
        self._status = "NOT STARTED"

    def start_execution(self) -> None:
        """Initialize execution timing and create the report file."""
        LOGS_DIRECTORY.mkdir(parents=True, exist_ok=True)

        self._start_time = perf_counter()
        self._execution_start = datetime.now()
        self._last_checkpoint = None
        self._status = "RUNNING"

        report_header = [
            "Selenium Automation Toolkit - Execution Report",
            "=" * 55,
            f"Application Version : {APPLICATION_VERSION}",
            f"Execution Start Time: {self._execution_start.isoformat()}",
            "",
            "Execution Checkpoints",
            "-" * 55,
        ]

        self._write_lines(report_header)

    def checkpoint(self, message: str) -> None:
        """Record a successful execution checkpoint."""
        self._last_checkpoint = message
        self._write_lines([f"[PASS] {message}"])

    def fail(self, message: str, error: Optional[Exception] = None) -> None:
        """Record a failed execution checkpoint and associated error."""
        self._status = "FAIL"

        lines = [f"[FAIL] {message}"]

        if error is not None:
            lines.append(f"Error: {error}")

        self._write_lines(lines)

    def complete_execution(self, success: bool = True) -> None:
        """Finalize the execution report with status and duration."""
        if self._start_time is None:
            raise RuntimeError("Execution has not been started.")

        duration = perf_counter() - self._start_time

        if success and self._status != "FAIL":
            self._status = "PASS"
        elif not success:
            self._status = "FAIL"

        completion_time = datetime.now()

        lines = [
            "",
            "Execution Summary",
            "-" * 55,
            f"Execution End Time  : {completion_time.isoformat()}",
            f"Status              : {self._status}",
            f"Last Successful Checkpoint: "
            f"{self._last_checkpoint or 'None'}",
            f"Execution Duration  : {duration:.3f} seconds",
        ]

        self._write_lines(lines)

    def _write_lines(self, lines: list[str]) -> None:
        """Append report lines to the execution report."""
        LOGS_DIRECTORY.mkdir(parents=True, exist_ok=True)

        with Path(EXECUTION_REPORT_PATH).open(
            "a",
            encoding="utf-8",
        ) as report_file:
            for line in lines:
                report_file.write(f"{line}\n")