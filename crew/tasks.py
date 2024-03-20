from crewai import Task
from datetime import datetime


class PurchaseAnalysisAutomationTasks():
    """Pool of tasks for the purchase analysis automation"""

    def data_categorization(self,
                            description: str,
                            agent: str,
                            expected_output: str,
                            output_file: str):
        return Task(
            description=description,
            agent=agent,
            expected_output=expected_output,
            output_file=output_file
        )

    def data_review(self,
                    description: str,
                    agent: str,
                    expected_output: str,
                    output_file: str):
        return Task(
            description=description,
            agent=agent,
            expected_output=expected_output,
            output_file=output_file
        )
