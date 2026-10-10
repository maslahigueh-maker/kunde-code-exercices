"""
config.py — the ONLY place secret keys are read from environment
variables. Nothing else in this project should read env vars directly.

TODO:
- load Supabase URL + service key

"""
from dotenv import load_dotenv
import os

load_dotenv()
# * use the env file to figure out what to put here. rmb the api keys are SECRET and should never just be in documents that are on github. What's the best way to use the value of something, without always copying said value...
# SUPABASE_KEY = os.getenv(__________)
# SUPABASE_URL = os.getenv(__________)
