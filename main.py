from config import *
from crew.agents import PurchaseAgents
from crew.tasks import PurchaseAnalysisAutomationTasks
from models.models import LargeLanguageModel
from crewai import Crew, Process
from crewai_tools import CSVSearchTool
from datetime import datetime


# Determine data tool
data_tool = CSVSearchTool("purchases.csv")


# Instantiate Models, Agents and Task

model = LargeLanguageModel()
agents = PurchaseAgents()
tasks = PurchaseAnalysisAutomationTasks()


models = {'openai': model.chat_Openai(temp=0.6),
          'gemini': model.gemini(temp=0.6),
          'mixtral': model.mixtral_groq(temp=0.6),
          'sonnet': model.claude3_sonnet(temp=0.6),
          'opus': model.claude3_opus(temp=0.6)}

# Initialize the Models, Agentes and Tasks
senior_analyst = agents.data_senior_analyst(
    goal=data_senior_analyst_goal,
    backstory=data_senior_analyst_backstory,
    tools=[data_tool],
    model=models['opus'],
    allow_delegation=False
)

junior_analyst = agents.data_junior_analyst(
    goal=data_junior_analyst_goal,
    backstory=data_junior_analyst_backstory,
    tools=[data_tool],
    model=models['openai'],
    allow_delegation=False
)

determine_categories = tasks.data_categorization(
    description=data_senior_analyst_tasks['task1'],
    agent=senior_analyst,
    expected_output=f"""A table showing the categories as well as the list of
    products that conform each category and are part of the list of purched items.
    
    #Table format:
    Header : Category | Products
    Rows: Category name | List of the products that belong to the this category
    """,
    output_file=f"outputs/{list(models.keys())[0]}-{datetime.now().strftime('%m-%d-%Y_%H:%M')}_categories.csv"
)

total_amount = tasks.data_review(
    description=data_junior_analyst_tasks['task1'],
    agent=junior_analyst,
    expected_output=f"""A value with the subtitle 'Total amount:'""",
    output_file=f"outputs/{list(models.keys())[0]}-{datetime.now().strftime('%m-%d-%Y_%H:%M')}_amount.csv"
)

calculate_subtotals = tasks.data_review(
    description=data_junior_analyst_tasks['task2'],
    agent=junior_analyst,
    expected_output=f"""A table with categories and money spent for each category""",
    output_file=f"outputs/{list(models.keys())[0]}-{datetime.now().strftime('%m-%d-%Y_%H:%M')}_amount.csv"
)
# Create the crew
crew = Crew(
    agents=[senior_analyst],
    tasks=[determine_categories],
    process=Process.sequential
)

# Kick Off the Crew
crew.kickoff()
