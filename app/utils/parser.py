import json
import re


import json

def parse_json(text):

    if isinstance(text, list):
        text = "\n".join(
            item.get("text", "")
            for item in text
            if item.get("type") == "text"
        )

    if not isinstance(text, str):
        raise TypeError(f"Expected str or list, got {type(text)}")

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)