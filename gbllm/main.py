""" Application entry point. """
import logging
import os

from langchain.llms import OpenAI
from gbllm.config import check_openai_api_key, Config
from gbllm.genbank.util import genbank_record_generator


def run_gbllm(
    instruction: str,
    genbank: str,
    model_name: str = 'text-ada-001',
    temperature: float = 0.9,
    debug: bool = False,
):
    # Configure the logging level.
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # Check that the OpenAI API key is set.
    config = Config()
    check_openai_api_key()

    # Initialize the OpenAI language model.
    llm = OpenAI(model_name=model_name, temperature=temperature)

    # Load the large genbank file and intialize a generator to iterate records in the file.
    generator = genbank_record_generator(genbank)

    # Load an agent
    from gbllm.agent.agent import Agent
    agent = Agent()