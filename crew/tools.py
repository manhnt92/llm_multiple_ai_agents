import os
from dotenv import load_dotenv
from crewai_tools import BaseTool, SerperDevTool, CodeInterpreterTool
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain_groq import ChatGroq

os.environ['SERPER_API_KEY'] = ''
tool = SerperDevTool()

class DuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGo"
    description: str = "Useful to browse information from the internet to know recent results and information you don't know. Then, tell user the result."
    ddg_search : DuckDuckGoSearchAPIWrapper = DuckDuckGoSearchAPIWrapper()

    def _run(self, argument: str) -> str:
        # """Search the web for information on a given topic"""
        return self.ddg_search.run(argument)
    
ddgTool = DuckDuckGoTool()