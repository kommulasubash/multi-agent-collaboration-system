
from crewai import Agent


def create_writer(mcp_tools, llm):

    writer = Agent(
        role="Technical Research Writer",

        goal=(
            "Transform research findings and "
            "analytical insights into a clear, "
            "structured, professional report."
        ),

        backstory=(
            "You are an expert technical writer "
            "who communicates complex information "
            "clearly. You organize findings into "
            "well-structured reports with summaries, "
            "insights, and conclusions."
        ),

        tools=mcp_tools,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    return writer
