from numpy import mean
from crewai.knowledge import knowledge
from mcp.server import FastMCP
from datetime import datetime
import json

# now we are intializing our mcp server
mcp = FastMCP("COLLABRATIVE RESEARCH MCP")


@mcp.tool()
def search_knowledge(query:str):
    """search the knowledge base for information relevant to research query."""
    knowledge_base = {
        "agentic ai":(
            "Agentci ai systems use llms to reason,"
            "plan,and execute actions using tools"
            "they often operate autonomously, but can be supervised by humans"
        ),
        "multi agent system":(
            "Multi-agent systems coordinate specialized "
            "AI agents to solve complex tasks."
        ),
        "crewai":(
              "CrewAI is a framework for orchestrating "
            "role-based AI agents and collaborative tasks."
        ),
        "mcp":(
            "Model Context Protocol is a standardized "
            "protocol for connecting AI applications "
            "with external tools and data sources."
        ),
        "rag":(
            "Retrieval-Augmented Generation combines "
            "information retrieval with LLM generation."
        )

    }
    results = []

    for key,value in knowledge_base.items():
        if key in query.lower() or query.lower() in key:
            results.append(value)
        
        if not results:
            return "no relevant data found for "+query
    
    return "\n".join(results)

@mcp.tool()
def calculate_statistics(numbers:list[float]) -> dict:
    """
    Calculate basic statistical information
    for a list of numerical values.
    """
    if not numbers:
        return {"error":" the list of numbers cannot be empty"}

    return {
        "count":len(numbers),
        "sum":sum(numbers),
        "min":min(numbers),
        "max":max(numbers),
        "mean":mean(numbers),

    }

@mcp.tool()
def save_search_notes(topic:str,content:str)->str:
    "save research note as local file json"

    filename = "research_notes.json"

    try:
        with open(filename,"r",encoding="utf-8") as file:
            notes = json.load(file)
            
    except(FileNotFoundError,json.JSONDecodeError):
        notes = []

    note  = {
        "topic":topic,
        "content":content,
        "createdat":datetime.now().isoformat()

    }    
    notes.append(note)

    with open(filename,"w",encoding="utf-8") as file:
        json.dump(notes,file,indent=4,ensure_ascii=False)
        

    return f"Note saved {topic}"

if __name__=="__main__":
    mcp.run(transport="stdio")