from multiprocessing import Queue as MPQueue
from queue import Queue
from typing import TYPE_CHECKING, Any

from enums import ComponentType

if TYPE_CHECKING:
    from .app import App


class Component:
    """
    A Discord Bot Engine Component.
    """
    def __init__(self, name: str, type: ComponentType) -> None:
        """
        Constructor.

        :param name: Display name of the Component. The name must be unique.
        :type name: str
        :param type: The type of the Component.
        :type type: ComponentType
        """
        self.name = name
        self.type = type

    def run(self, app: "App", queue: Queue[Any] | MPQueue[Any]) -> None:
        self.app = app
        self.queue = queue
        self.start()

    def start(self) -> None:
        pass
