import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


def create_explainer():

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are a smart product recommendation assistant.

            Explain why the recommended products match the
            user's requirements.

            Mention:
            - User's budget
            - Important features
            - Product strengths
            - Why the product is suitable

            Keep the explanation simple and concise.

            Do not invent specifications that are not provided.
            """
        ),
        (
            "human",
            """
            User requirements:
            {preferences}

            Recommended products:
            {products}

            Explain the recommendations.
            """
        )
    ])

    return prompt | llm


def explain_recommendations(preferences, products):

    explainer = create_explainer()

    result = explainer.invoke({
        "preferences": preferences,
        "products": products
    })

    return result.content