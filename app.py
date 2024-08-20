from crewai import Crew, Process
from crew.tasks import research_task, analysis_task, writing_task, coding_task
from crew.agents import researcher, analyst, writer, python_engineer

def main():
    # crew = Crew(
    #     agents=[researcher, analyst, writer],
    #     tasks=[research_task, analysis_task, writing_task],
    #     process=Process.sequential,
    # )
    # # result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
    # print(result)

    crew1 = Crew(
        agents=[python_engineer],
        tasks=[coding_task]
    )
    result = crew1.kickoff(inputs={'topic': 'SOLVING EQUAION X^2-2*X+1=0'})
    print(result)

if __name__ == "__main__":
    main()