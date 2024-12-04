from argparse import Namespace, ArgumentParser
import os
from src.hello_azure_ai_foundry.ai.search import create_index_from_csv
from src.hello_azure_ai_foundry.utils.config import get_logger

# initialize logging object
logger = get_logger(__name__)


def run(args: Namespace) -> None:
    index_name: str = args.index_name
    csv_file: str = args.csv_file

    create_index_from_csv(index_name, csv_file)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--index-name",
        type=str,
        help="index name to use when creating the AI Search index",
        default=os.environ["AISEARCH_INDEX_NAME"],
    )

    parser.add_argument(
        "--csv-file", type=str, help="path to data for creating search index", default="assets/products.csv"
    )

    args:Namespace = parser.parse_args()

    run(args.index_name, args.csv_file)
