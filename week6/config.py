"""
config.py — the ONLY place secret keys are read from environment
variables. Nothing else in this project should read env vars directly.

TODO:
- load Supabase URL + service key

"""
from dotenv import load_dotenv
import os

load_dotenv()
# * use the env file to figure out what to put here. rmb the api keys are SECRET and should never just be in documents that are on github.
# SUPABASE_KEY = os.getenv(_______)
# SUPABASE_URL = os.getenv(_______)



# AWS_KEY_ID = os.getenv(_______)
# AWS_KEY = os.getenv(_______)
# AWS_REGION = os.getenv(_______)
