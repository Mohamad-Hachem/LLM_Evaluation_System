import RAG4.tools as tl

from .prompts import system_agent_prompt
from langchain_openai import ChatOpenAI
from .tools import collecting_info2
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from .objects import Answer


llm = ChatOpenAI(model="gpt-4o", temperature=0)

agent = create_agent(
    model=llm,
    tools=[collecting_info2],
    system_prompt=system_agent_prompt,
    response_format=Answer
)

def ask(question) -> dict:
    """Answer the user's question about the PDF."""

    # Reset it so we don't accidentally use context
    # from the previous question
    tl.last_retrieved_context = []

    result = agent.invoke({
        "messages": [HumanMessage(content=question)]
    })

    structured_response = result["structured_response"]

    return {
        "answer": structured_response.answer,
        "retrieval_context": tl.last_retrieved_context
    }

#print(ask("How do penguin partners recognize one another during courtship?"))
