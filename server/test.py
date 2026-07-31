from app.planner.planner import ExecutivePlanner

planner = ExecutivePlanner()

tests = [
    "hello",
    "tell me a joke",
    "my dog's name is max",
    "what's my dog's name",
    "no my dog's name is leon",
    "tell me about me",
    "do you know who i am",
    "print this pdf",
    "52*91",
    "who is prime minister of india",
]

for t in tests:
    print(f"\nUSER: {t}")
    res = planner.plan(t)
    print(f"INTENT: {res['intent']} (Memory: {res['needs_memory']}, Chat: {res['needs_chat']}, Web: {res['needs_web']})")