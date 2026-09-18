from crewai import LLM

llm = LLM(
    model="gemini/gemini-3.6-flash"
)

response = llm.call("Say hello in one sentence.")

print(response)