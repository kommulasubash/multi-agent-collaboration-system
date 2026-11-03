from crewai import Agent


def create_coordinator(llm):

    coordinator = Agent(
        role="Senior Research Coordinator",
        goal=(
            "Understand the user's research topic, define "
            "the research objectives, coordinate the "
            "research team, and ensure the final report "
            "answers the user's question comprehensively."
        ),
        backstory=(
            "You are an experienced research project "
            "manager who specializes in breaking complex "
            "problems into manageable research tasks. "
            "You understand how to coordinate researchers, "
            "analysts, and technical writers to produce "
            "high-quality, evidence-based reports."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=True
    )

    return coordinator

