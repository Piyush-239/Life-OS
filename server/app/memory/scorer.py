class ImportanceScorer:

    CATEGORY_SCORES = {
        "personal": 10,
        "identity": 10,
        "education": 8,
        "career": 8,
        "goal": 9,
        "relationship": 9,
        "health": 9,
        "location": 7,
        "preference": 3,
        "hobby": 4,
        "entertainment": 2,
    }

    def score(self, memory):

        return self.CATEGORY_SCORES.get(
            memory["category"],
            5,
        )
