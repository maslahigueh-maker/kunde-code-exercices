"""
services/embeddings.py — calls AWS Bedrock, returns an embedding

The "3 lines that matter." Takes text, returns a list of numbers.
This is the ONLY file that should know Bedrock exists.

See: docs/kunde_code_build_guide.md — Section 5
See: docs/whitney_personal_roadmap.md — Week 2, Step 5

"""
from config import AWS_REGION
import json
import boto3


def get_embedding( text, input_type="search_document"):
    client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

    response = client.invoke_model(
        modelId="cohere.embed-multilingual-v3",
        body=json.dumps(
            {
                # added the brackets so the input can be sent as a text instead of having to be in an array
                "texts": [text],
                "input_type":input_type,
            }
        ),
    )
    body = response["body"].read()
    # print("RAW RESPONSE:", body)
    result = json.loads(body)
    return result["embeddings"][0]

