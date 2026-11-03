
from crewai import Agent


def create_researcher(mcp_tools, llm):

    researcher = Agent(
        role="AI Research Specialist",

        goal=(
            "Research the assigned topic thoroughly "
            "and gather accurate, relevant information "
            "using available MCP tools."
        ),

        backstory=(
            "You are an experienced AI researcher "
            "specializing in technology, AI, and "
            "emerging innovations. You gather evidence, "
            "identify important concepts, and provide "
            "reliable research findings."
        ),

        tools=mcp_tools,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    return researcher
