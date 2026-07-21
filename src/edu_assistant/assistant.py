from pathlib import Path

from edu_assistant.config import Config, RoleType, TemplateType
from edu_assistant.llm_client import get_llm_client


def create_response(
    llm_key: str,
    role: RoleType,
    template: TemplateType,
    prompt: str,
    config_path: str | Path = "config.yml",
) -> str:
    # Загружаем конфиг
    config = Config.from_yaml_file(config_path)

    # Получаем настройки выбранной модели
    llm_config = config.llms[llm_key]

    # Собираем системную инструкцию
    system_instruction = config.render_system_instructions(
        role=role,
        template=template,
    )

    # Создаём клиента
    llm_client = get_llm_client(llm_config=llm_config)

    # Отправляем запрос через Chat Completions API
    response = llm_client.chat.completions.create(
        model=llm_config.model,
        messages=[
            {
                "role": "system",
                "content": system_instruction,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=llm_config.max_output_tokens,
    )

    return response.choices[0].message.content or ""