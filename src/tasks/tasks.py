
from crewai import Task


def create_research_task(researcher, topic):

    return Task(
        description=(
            f"Research the following topic: {topic}\n\n"
            "Use the available MCP knowledge search "
            "tool when relevant.\n"
            "Gather definitions, important concepts, "
            "applications, and current challenges.\n"
            "Provide organized research findings."
        ),

        expected_output=(
            "A comprehensive research document "
            "containing key information, concepts, "
            "applications, and relevant findings."
        ),

        agent=researcher
    )


def create_analysis_task(analyst, research_task):

    return Task(
        description=(
            "Analyze the researcher's findings provided "
            "in the context below.\n"
            "Identify important insights, patterns, "
            "advantages, limitations, and knowledge gaps.\n"
            "Use the available MCP statistics tool "
            "if numerical analysis is appropriate.\n"
            "Do not invent facts or statistics."
        ),

        expected_output=(
            "A structured analytical report with "
            "insights, findings, limitations, "
            "and conclusions."
        ),

        agent=analyst,

        context=[research_task]
    )


def create_writing_task(writer, research_task, analysis_task):

    return Task(
        description=(
            "Combine the research findings and "
            "analytical insights provided in the context "
            "below into a final report.\n"
            "Include an executive summary, key "
            "findings, analysis, applications, "
            "challenges, and conclusion.\n"
            "Avoid unnecessary repetition."
        ),

        expected_output=(
            "A polished, comprehensive, readable "
            "research report in Markdown format."
        ),

        agent=writer,

        context=[
            research_task,
            analysis_task
        ]
    )
