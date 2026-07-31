def normalize_key(key: str) -> str:
    # lower case, remove punctuation/possessives, replace underscores/spaces with empty string
    k = key.lower().strip()
    k = k.replace("'s", "")
    k = k.replace("'", "")
    k = k.replace("_", "")
    k = "".join(k.split())
    return k
