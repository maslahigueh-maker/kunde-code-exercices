from dotenv import load_dotenv
import os

import boto3

load_dotenv(override=True)



SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")

AWS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MANSA_API_BASE_URL = os.getenv("MANSA_API_BASE_URL")
MANSA_API_KEY = os.getenv("MANSA_API_KEY")

# session = boto3.Session(
#     aws_access_key_id= AWS_KEY_ID,
#     aws_secret_access_key= AWS_KEY,
#     region_name="us-east-1",
# )

# print(session.client("sts").get_caller_identity()["Arn"])