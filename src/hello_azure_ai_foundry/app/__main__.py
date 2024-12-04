from argparse import ArgumentParser, Namespace

from src.hello_azure_ai_foundry.app.ai.chat import run as run_chat
from src.hello_azure_ai_foundry.config import get_logger, set_telemetry

logger = get_logger(__name__)


def run(query: str, use_telemetry: bool):
    logger.info("Starting hello-azure-ai-foundry...")
    logger.info("query='{%s}'", query)

    # enable telemetry if requested
    set_telemetry(use_telemetry)

    # run the chat
    run_chat(query)


if __name__ == "__main__":
    # load command line arguments
    parser = ArgumentParser()

    parser.add_argument(
        "--query",
        type=str,
        help="Query to use to search product",
        default="I need a new tent for 4 people, what would you recommend?")

    parser.add_argument(
        "--enable-telemetry",
        action="store_true",
        help="Enable sending telemetry back to the project",
        default=False)

    args: Namespace = parser.parse_args()
    use_telemetry: bool = args.enable_telemetry
    query: str = args.query

    run(query, use_telemetry)
