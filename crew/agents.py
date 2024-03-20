from crewai import Agent


class PurchaseAgents():
    """Pool of agents for the Purchase Analyze Process"""

    def data_senior_analyst(self,
                            goal: str,
                            backstory: str,
                            tools: [],
                            model,
                            allow_delegation: bool):
        return Agent(
            role="Data Senior Analyst",
            goal=goal,
            backstory=backstory,
            llm=model,
            tools=tools,
            allow_delegation=allow_delegation,
            verbose=True
        )

    def data_junior_analyst(self,
                            goal: str,
                            backstory: str,
                            tools: [],
                            model,
                            allow_delegation: bool):
        return Agent(
            role="Data Junior Analyst",
            goal=goal,
            backstory=backstory,
            llm=model,
            tools=tools,
            allow_delegation=allow_delegation,
            verbose=True
        )
