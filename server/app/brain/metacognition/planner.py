class Planner:

    def plan(self, message: str):

        message = message.lower()

        plan = {
            "retrieve_memory": False,
            "use_tools": False,
            "ask_clarification": False,
        }

        memory_keywords = [

            "my",

            "me",

            "myself",

            "remember",

            "favorite",

            "name",

            "who am i",

            "about me",

            "goal",

            "study",

            "college",

            "friend",

            "drink",

            "hobby",

            "birthday",
        ]

        tool_keywords = [

            "print",

            "send",

            "email",

            "open",

            "call",

            "search",

            "download",

            "play",

            "turn on",

            "turn off",
        ]

        for keyword in memory_keywords:

            if keyword in message:

                plan["retrieve_memory"] = True
                break

        for keyword in tool_keywords:

            if keyword in message:

                plan["use_tools"] = True
                break

        return plan