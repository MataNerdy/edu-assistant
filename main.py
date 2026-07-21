from pathlib import Path
import yaml

# Папка, в которой находится main.py
project_dir = Path(__file__).resolve().parent

# config.yml рядом с main.py
config_path = project_dir / "config.yml"

config_str = config_path.read_text(encoding="utf-8")
config = yaml.safe_load(config_str)

print(config)