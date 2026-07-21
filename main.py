from dotenv import load_dotenv

from edu_assistant.assistant import create_response

load_dotenv()

INPUT_PROMPT = input()

response = create_response(
    llm_key="mistral",
    role="history_tutor",
    template="tutor_full_answer",
    prompt=INPUT_PROMPT,
)

print(response)