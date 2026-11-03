# Multi-Agent Collaboration System

An intelligent multi-agent research and synthesis framework powered by [CrewAI](https://github.com/crewAIInc/crewAI) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

## Overview

This project implements a collaborative team of specialized AI agents designed to autonomously research, analyze, synthesize, and produce comprehensive research reports:

- **Senior Research Coordinator**: Clarifies research goals, coordinates team delegation, and ensures overall quality.
- **Research Specialist**: Gathers factual information, queries custom MCP tools, and records findings.
- **Data & Insights Analyst**: Evaluates source reliability, identifies patterns, synthesizes insights, and structures findings.
- **Technical Writer**: Compiles analyzed research into clear, structured, and publication-ready markdown reports.

## Architecture

- **CrewAI**: Manages agent collaboration, task dependencies, and sequential execution.
- **MCP Server**: Custom Model Context Protocol server exposing specialized tools for research and local knowledge retrieval.
- **OpenRouter LLM Integration**: Flexible LLM backend (e.g. Nvidia Nemotron, Claude, GPT-4, etc.) via OpenRouter.

## Project Structure

```text
├── src/
│   ├── agents/
│   │   ├── coordinator.py   # Research coordinator agent
│   │   ├── researcher.py    # Primary researcher agent
│   │   ├── analyst.py       # Data analyst agent
│   │   └── writer.py        # Technical report writer agent
│   ├── tasks/
│   │   └── tasks.py         # Task definitions and dependency mapping
│   ├── mcp_server/
│   │   └── server.py        # Custom MCP server exposing tools
│   ├── tools/
│   │   └── mcp_client.py    # MCP client configuration & utilities
│   └── main.py              # Main execution entrypoint
├── .env.example             # Example environment variables
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Getting Started

### 1. Prerequisites

- Python 3.10+
- OpenRouter API key

### 2. Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/kommulasubash/multi-agent-collaboration-system.git
cd multi-agent-collaboration-system

python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configuration

Copy `.env.example` to `.env` and fill in your OpenRouter API key:

```bash
cp .env.example .env
```

Update `.env`:
```env
OPENROUTER_API_KEY=your_api_key_here
MODEL_NAME=openrouter/nvidia/nemotron-3-ultra-550b-a55b:free
```

### 4. Running the System

Execute the collaborative crew:

```bash
python -m src.main
```

Enter your research topic when prompted. The team of agents will coordinate, research, analyze, and output a completed report saved to `final_research_report.md`.
