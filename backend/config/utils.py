from os import environ

from dotenv.main import load_dotenv

from backend.config.default import DefaultSettings


def get_settings() -> DefaultSettings:
    env = environ.get("ENV", "local")
    if env == "local":
        load_dotenv()
        return DefaultSettings()
    return DefaultSettings()
