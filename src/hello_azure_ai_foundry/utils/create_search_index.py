from argparse import Namespace, ArgumentParser
import os
from src.hello_azure_ai_foundry.ai.search import create_index_from_csv
from src.hello_azure_ai_foundry.config import get_logger

# initialize logging object
logger = get_logger(__name__)


def run(*args) -> None:
    create_index_from_csv(*args)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--index-name", type=str, help="index name to use when creating the AI Search index", default=os.environ["AISEARCH_INDEX_NAME"])
    parser.add_argument("--csv-file", type=str, help="path to data for creating search index", default="assets/products.csv")

    args:Namespace = parser.parse_args()
    index_name: str = args.index_name
    csv_file: str = args.csv_file

    run(index_name, csv_file)
