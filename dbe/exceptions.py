class DiscordBotEngineException(Exception):
    pass


class ComponentError(DiscordBotEngineException):
    pass


class DuplicatedComponentNameError(ComponentError):
    pass
