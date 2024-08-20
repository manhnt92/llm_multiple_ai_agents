import os
from crewai import Agent
from tools import tool
from langchain import hub, LLMMathChain
from langchain_google_genai import ChatGoogleGenerativeAI, HarmCategory, HarmBlockThreshold
from langchain_huggingface import HuggingFaceEndpoint
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = ""

# call gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    convert_system_message_to_human=True,
    handle_parsing_errors=True,
    temperature=0.0,
    max_tokens= 200,
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    },
) 

codingLLM = ChatGroq(
    temperature=0, 
    groq_api_key = '', 
    model_name='llama3-8b-8192'
)

researcher = Agent(
  role='Researcher',
  goal='Conduct foundational research',
  backstory='An experienced researcher with a passion for uncovering insights',
  tools=[tool],
  llm=llm,
  verbose=True,
  memory=True,
  allow_delegation=True
)

analyst = Agent(
  role='Data Analyst',
  goal='Analyze research findings',
  backstory='A meticulous analyst with a knack for uncovering patterns',
  llm=llm,
  verbose=True,
  allow_delegation=True
)

writer = Agent(
  role='Writer',
  goal='Draft the final report',
  backstory='A skilled writer with a talent for crafting compelling narratives',
  llm=llm,
  verbose=True,
)

python_engineer = Agent(
    role="Senior Python Developer",
    goal="Write a python script to solve the task with proper OOP principles.",
    backstory="You are a senior Python developer with strong Python skills",
    llm=llm,
    tool=[codingLLM],
    allow_code_execution=True,
    verbose=True,
)