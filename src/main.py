import os

from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from mcp import StdioServerParameters
from crewai_tools import MCPServerAdapter

from src.agents.coordinator import create_coordinator
from src.agents.researcher import create_researcher
from src.agents.analyst import create_analyst
from src.agents.writer import create_writer

from src.tasks.tasks import (
    create_research_task,
    create_analysis_task,
    create_writing_task
)


load_dotenv()


def main():

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError(
            "Please configure OPENROUTER_API_KEY in .env"
        )

    llm = LLM(
        model=os.getenv(
            "MODEL_NAME",
            "nvidia/nemotron-3-ultra-550b-a55b:free"
        ),
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    # Connect CrewAI to our custom MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["src/mcp_server/server.py"]
    )

    print("\nConnecting to MCP server...\n")

    with MCPServerAdapter(server_params) as mcp_tools:

        print("MCP tools discovered:")

        for tool in mcp_tools:
            print(f"- {tool.name}")

        # Create specialized agents
        coordinator = create_coordinator(llm)

        researcher = create_researcher(
            mcp_tools, llm
        )

        analyst = create_analyst(
            mcp_tools, llm
        )

        writer = create_writer(
            mcp_tools, llm
        )

        # Get research topic
        topic = input(
            "\nEnter a research topic: "
        )

        # Create sequential tasks
        research_task = create_research_task(
            researcher, topic
        )

        analysis_task = create_analysis_task(
            analyst,
            research_task
        )

        writing_task = create_writing_task(
            writer,
            research_task,
            analysis_task
        )

        # Assemble the collaborative crew
        crew = Crew(
            agents=[
                coordinator,
                researcher,
                analyst,
                writer
            ],

            tasks=[
                research_task,
                analysis_task,
                writing_task
            ],

            process=Process.sequential,
            verbose=True
        )

        print("\nStarting collaborative research...\n")

        result = crew.kickoff()

        # Save report
        with open(
            "final_research_report.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(str(result))

        print("\nResearch completed!")
        print("\nReport saved to final_research_report.md")


if __name__ == "__main__":
    main()
