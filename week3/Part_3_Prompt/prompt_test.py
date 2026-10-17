from pathlib import Path

from config import AWS_KEY_ID, AWS_KEY, AWS_REGION
from botocore.config import Config
import boto3


def get_answer(
    prompt,
    system_prompt="You are a helpful AI assistant.",
    output_folder=None,
    max_tokens=8000,
):
    if not system_prompt:
        system_prompt = "You are a helpful AI assistant."

    bedrock = boto3.client(
        "bedrock-runtime",
        region_name=AWS_REGION,
        config=Config(read_timeout=300),
    )

    # Calling the model
    response = bedrock.converse(
        modelId="us.amazon.nova-2-lite-v1:0",
        messages=[
            {
                "role": "user",
                # ^ this is where we send your prompt to AWS
                "content": [{"text": prompt}],
            }
        ],
        system=[{"text": system_prompt}],
        # Without this, long answers get cut off mid-sentence.
        inferenceConfig={"maxTokens": max_tokens},
    )

    # Warn if the model hit the limit and the answer is incomplete
    if response.get("stopReason") == "max_tokens":
        print(f"WARNING: answer was cut off at {max_tokens} tokens")

    # Extract the text response, previewing in terminal
    content_list = response["output"]["message"]["content"]
    answer = ""
    for content in content_list:
        if "text" in content:
            print(content["text"])
            answer += content["text"]

    # Save output to the group's folder
    if output_folder:
        output_path = Path(output_folder) / "ai_output.md"
        output_path.write_text(answer, encoding="utf-8")
        print(f"\nSaved output to: {output_path}")

    return answer