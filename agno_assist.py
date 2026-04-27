from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

agno_assist = Agent(
    name="Agno Assist",
    model=Claude(id="claude-sonnet-4-5"),
    db=SqliteDb(db_file="agno.db"),                     # session storage
    tools=[MCPTools(url="https://docs.agno.com/mcp")],  # Agno docs via MCP
    add_datetime_to_context=True,
    add_history_to_context=True,                         # include past runs
    num_history_runs=3,                                  # last 3 conversations
    markdown=True,
)

# Serve via AgentOS → streaming, auth, session isolation, API endpoints
agent_os = AgentOS(agents=[agno_assist], tracing=True)
app = agent_os.get_app()