import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


class UserPreferences(BaseModel):
    category: str = Field(
        description="Product category requested by the user"
    )

    budget: float = Field(
        description="Maximum budget in Indian rupees"
    )

    camera_priority: float = Field(
        description="Camera importance from 0 to 1"
    )

    battery_priority: float = Field(
        description="Battery importance from 0 to 1"
    )

    performance_priority: float = Field(
        description="Performance importance from 0 to 1"
    )

    display_priority: float = Field(
        description="Display importance from 0 to 1"
    )


def create_parser():

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )

    structured_llm = llm.with_structured_output(
        UserPreferences
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are a product requirement extraction assistant.

            Understand the user's natural-language product request
            and extract their requirements.

            Convert priorities into values between 0 and 1.

            Examples:

            Very important = 0.9
            Important = 0.75
            Moderate = 0.5
            Low importance = 0.25

            If the user does not mention a particular feature,
            use 0.5.

            Extract the maximum budget in Indian rupees.

            Do not recommend a product.
            Only understand and structure the user's requirements.
            """
        ),
        (
            "human",
            "{query}"
        )
    ])

    return prompt | structured_llm


def parse_user_query(query):

    parser = create_parser()

    result = parser.invoke({
        "query": query
    })

    return result