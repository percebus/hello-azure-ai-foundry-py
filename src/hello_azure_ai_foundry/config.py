# ruff: noqa: ANN201, ANN001

import logging
import os
import pathlib
import sys

from azure.ai.inference.tracing import AIInferenceInstrumentor
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.monitor.opentelemetry import configure_azure_monitor

# load environment variables from the .env file
from dotenv import load_dotenv

load_dotenv()

# Set "./assets" as the path where assets are stored, resolving the absolute path:
ASSET_PATH = pathlib.Path(__file__).parent.resolve() / "../../assets"

# Configure an root app logger that prints info level logs to stdout
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
# logger.propagate = True


# Returns a module-specific logger, inheriting from the root app logger
def get_logger(module_name):
    _logger = logging.getLogger(f"app.{module_name}")
    # _logger.propagate = False
    return _logger


# Enable instrumentation and logging of telemetry to the project
def set_telemetry(log_to_project: bool = False):
    logger.debug("set_telemetry: {%s}", log_to_project)
    AIInferenceInstrumentor().instrument()

    # enable logging message contents
    os.environ["AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED"] = "true"

    if log_to_project:
        project = AIProjectClient.from_connection_string(
            conn_str=os.environ["AIPROJECT_CONNECTION_STRING"], credential=DefaultAzureCredential()
        )
        tracing_link = f"https://ai.azure.com/tracing?wsid=/subscriptions/{project.scope['subscription_id']}/resourceGroups/{project.scope['resource_group_name']}/providers/Microsoft.MachineLearningServices/workspaces/{project.scope['project_name']}"
        application_insights_connection_string = project.telemetry.get_connection_string()
        if not application_insights_connection_string:
            logger.warning(
                "No application insights configured, telemetry will not be logged to project. Add application insights at:"
            )

            logger.warning(tracing_link)

            return

        configure_azure_monitor(connection_string=application_insights_connection_string)
        logger.info("Enabled telemetry logging to project, view traces at:")
        logger.info(tracing_link)