"""
Project : Selenium Automation Toolkit
Project ID : 025

Workflow Service
"""

from collections.abc import Callable
from typing import Any


class WorkflowService:
    """Provide reusable workflow execution."""

    def execute(
        self,
        workflow: Callable[..., Any],
        **kwargs: Any,
    ) -> Any:
        """Execute the supplied workflow with the given arguments."""
        return workflow(**kwargs)