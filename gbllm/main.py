""" Application entry point. """
import logging
import os

from langchain.llms import OpenAI
from gbllm.config import check_openai_api_key, Config


def run_gbllm(
    instruction: str,
    genbank: str,
    debug: bool = False,
):
    # Configure the logging level.
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # Check that the OpenAI API key is set.
    config = Config()
    check_openai_api_key()

    llm = OpenAI(temperature=0.9, model_name='text-ada-001')
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))