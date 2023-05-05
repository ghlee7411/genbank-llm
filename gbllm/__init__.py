import os
import random
import sys
from dotenv import load_dotenv

if "pytest" in sys.argv or "pytest" in sys.modules or os.getenv("CI"):
    print('Running in test mode')
    print('Setting the random seed to 0')
    random.seed(0)

# load the environment variables from the .env file in the root directory of the project
load_dotenv(verbose=True, override=True)
# delete the load_dotenv function from the namespace
del load_dotenv