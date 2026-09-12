"""
Project : Selenium Automation Toolkit
Project ID : 025

Application Entry Point
"""

from src.core.browser_automation import BrowserAutomation
from src.core.web_form_page import WebFormPage
from src.core.web_form_workflow import WebFormWorkflow
from src.services.browser_service import BrowserService
from src.services.logging_service import LoggingService
from src.services.workflow_service import WorkflowService


def main() -> None:
    """Run the Slice 2 reusable browser automation workflow."""
    logging_service = LoggingService()
    browser_service = BrowserService()
    workflow_service = WorkflowService()

    logging_service.start_execution()

    try:
        logging_service.checkpoint("Application initialized")

        browser_service.start()
        logging_service.checkpoint("Browser started")

        automation = BrowserAutomation(browser_service)

        page = WebFormPage(automation)
        workflow = WebFormWorkflow(page)

        workflow_result = workflow_service.execute(
            workflow.execute,
            text="Slice 2 test input",
        )

        logging_service.checkpoint(
            "Web Form workflow executed"
        )

        if not workflow_result:
            raise RuntimeError(
                "Web Form workflow verification failed."
            )

        logging_service.checkpoint(
            "Web Form workflow verification passed"
        )

        logging_service.complete_execution(
            success=True
        )

    except Exception as exc:
        logging_service.fail(
            "Slice 2 browser automation failed",
            error=exc,
        )
        logging_service.complete_execution(
            success=False
        )
        raise

    finally:
        browser_service.close()


if __name__ == "__main__":
    main()