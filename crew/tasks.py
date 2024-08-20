from crewai import Task
from tools import tool, ddgTool
from agents import researcher, analyst, writer, python_engineer

research_task = Task(description='Gather relevant data in {topic}', agent=researcher, expected_output='Raw Data')
analysis_task = Task(description='Analyze the data in {topic}', agent=analyst, expected_output='Data Insights')
writing_task = Task(description='Compose the report...', agent=writer, expected_output='Final Report')

coding_task = Task(
    description="write a python code for {topic}",
    expected_output="solution of the quadratic equation with values of unknown x",
    agent=python_engineer,
    output_file='output.py'
)