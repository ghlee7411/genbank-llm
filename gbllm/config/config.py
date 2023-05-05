import os
from typing import List, Optional, Tuple
import openai
import yaml
from gbllm.singleton import Singleton


class Config(metaclass=Singleton):
    """
    Configuration class for the gbllm package.
    """

    def __init__(self) -> None:
        """
        Initialize the configuration class.
        """
        self._config = self._load_config()

    def _load_config(self) -> None:
        """
        Load the configuration file.
        """
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        

def check_openai_api_key() -> None:
    """
    Check that the OpenAI API key is set.
    """
    config = Config()
    if config.openai_api_key is None:
        raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")