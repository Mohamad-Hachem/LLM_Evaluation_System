from pydantic import BaseModel, Field


class Answer(BaseModel):
    answer:str = Field(description="The answer that is needed for the User's question")
    context:str = Field(description="A small citation of where the info was found")