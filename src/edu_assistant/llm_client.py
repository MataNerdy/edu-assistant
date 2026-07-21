import os

from openai import OpenAI

from edu_assistant.config import LLMConfig


def get_llm_client(llm_config: LLMConfig) -> OpenAI:
    if llm_config.api_key_env is None:
        # Ollama не проверяет ключ, но OpenAI SDK требует непустое значение
        api_key = "ollama"
    else:
        api_key = os.getenv(llm_config.api_key_env)

        if not api_key:
            raise ValueError(
                f"Не найдена переменная окружения "
                f"{llm_config.api_key_env}"
            )

    return OpenAI(
        api_key=api_key,
        base_url=llm_config.base_url,
        timeout=llm_config.timeout,
    )