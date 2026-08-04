import json
import re


def parse_json(text: str) -> dict:
    """
    Extract JSON from an LLM response.
    """

    if not text:
        return {}

    # Remove markdown code fences
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Try direct parsing
    try:
        return json.loads(text)
    except Exception:
        pass

    # Extract first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except Exception:
            pass

    return {}