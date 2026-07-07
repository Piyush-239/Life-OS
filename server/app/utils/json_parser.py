import json


def parse_llm_json(response: str):

    if not response:
        return []

    response = response.strip()

    print("\n========== RAW LLM ==========")
    print(response)
    print("=============================\n")

    if response.startswith("```"):
        response = response.split("\n", 1)[1]
        response = response.rsplit("```", 1)[0]

    response = response.strip()

    try:
        result = json.loads(response)

        if isinstance(result, dict):
            return [result]

        if isinstance(result, list):
            return result

        return []

    except Exception as e:

        print("JSON ERROR")
        print(e)

        return []