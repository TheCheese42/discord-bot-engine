from enum import StrEnum


class ComponentType(StrEnum):
    DISCORD_BOT = "DISCORD_BOT"
    PYTHON_SCRIPT = "PYTHON_SCRIPT"
    DATABASE_MODEL = "DATABASE_MODEL"
    IN_MEMORY_DATABASE = "IN_MEMORY_DATABASE"
    BACKGROUND_JOB = "BACKGROUND_JOB"
    ARBITRARY_EXECUTABLE = "ARBITRARY_EXECUTABLE"
