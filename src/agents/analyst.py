
from crewai import Agent


def create_analyst(mcp_tools, llm):

    analyst = Agent(
        role="Research Data Analyst",

        goal=(
            "Analyze research findings, identify "
            "patterns, evaluate information, and "
            "produce meaningful insights."
        ),

        backstory=(
            "You are a critical-thinking analyst "
            "who evaluates research information, "
            "identifies gaps, validates conclusions, "
            "and converts raw findings into insights."
        ),

        tools=mcp_tools,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    return analyst
