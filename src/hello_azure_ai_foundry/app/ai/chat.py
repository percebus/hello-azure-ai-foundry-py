import os
from argparse import ArgumentParser, Namespace
from pathlib import Path

from azure.ai.inference.prompts import PromptTemplate
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from opentelemetry import trace

from src.hello_azure_ai_foundry.app.ai.rag.products import get_product_documents
from src.hello_azure_ai_foundry.config import ASSET_PATH, get_logger

# initialize logging and tracing objects
logger = get_logger(__name__)
tracer = trace.get_tracer(__name__)

# create a project client using environment variables loaded from the .env file
project = AIProjectClient.from_connection_string(
    conn_str=os.environ["AIPROJECT_CONNECTION_STRING"], credential=DefaultAzureCredential()
)

# create a chat client we can use for testing
chat = project.inference.get_chat_completions_client()



@tracer.start_as_current_span(name="chat_with_products")
def chat_with_products(messages: list, context: dict = None) -> dict:
    logger.debug("chat_with_products: messages='{%s}'", messages)

    if context is None:
        context = {}

    documents = get_product_documents(messages, context)

    # do a grounded chat call using the search results
    grounded_chat_prompt = PromptTemplate.from_prompty(Path(ASSET_PATH) / "grounded_chat/v1.prompty")

    system_message = grounded_chat_prompt.create_messages(documents=documents, context=context)
    response = chat.complete(
        model=os.environ["CHAT_MODEL"],
        messages=system_message + messages,
        **grounded_chat_prompt.parameters,
    )
    logger.info(f"💬 Response: {response.choices[0].message}")

    # Return a chat protocol compliant response
    return {"message": response.choices[0].message, "context": context}


def run(content: str):
    logger.info("🚀 Starting chat with products, for message '{%s}'", content)

    # run chat with products
    logger.info("🤖 Chatting with products...")
    response = chat_with_products(messages=[{"role": "user", "content": content}])

    logger.info("🎉 Done! Response: {%s}", response["message"])



if __name__ == "__main__":
    # load command line arguments
    parser = ArgumentParser()

    parser.add_argument(
        "--query",
        type=str,
        help="Query to use to search product",
        default="I need a new tent for 4 people, what would you recommend?")

    args:Namespace = parser.parse_args()
    query:str = args.query

    run(query)
