from .prompts import system_agent_prompt
from langchain_openai import ChatOpenAI
from .tools import collecting_info
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from .objects import Answer


llm = ChatOpenAI(model="gpt-4o", temperature=0)

agent = create_agent(
    model=llm,
    tools=[collecting_info],
    system_prompt=system_agent_prompt,
    response_format=Answer
)


def ask(question) -> dict:
    """This Function asnwer the User question about a PDF"""

    result = agent.invoke({"messages": [HumanMessage(content=question)]})

    return result["messages"][-1].content

#print(ask("Where do penguins live?"))