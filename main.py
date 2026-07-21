from dotenv import load_dotenv

from edu_assistant.assistant import create_response

load_dotenv()

INPUT_PROMPT = "Кто победил, печенеги или половцы?"

response = create_response(
    llm_key="ollama",
    role="history_tutor",
    template="tutor_quick_answer",
    prompt=INPUT_PROMPT,
)

print(response)