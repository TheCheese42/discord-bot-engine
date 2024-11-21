from multiprocessing import Process
from multiprocessing import Queue as MPQueue
from multiprocessing.pool import ThreadPool
from queue import Queue
from threading import Thread
from typing import Any

from .component import Component
from .exceptions import DuplicatedComponentNameError


class App:
    def __init__(self) -> None:
        self._components: list[Component] = []
        self._components_threads_queues: list[tuple[
            Component, Thread | Process | ThreadPool, Queue[Any] | MPQueue[Any]
        ]] = []

    def add_component(self, component: Component) -> None:
        """
        Add a component to the internal list of components.

        :param component: A Discord Bot Engine Component
        :type component: Component
        """
        self._components.append(component)

    def remove_component(self, component: Component) -> None:
        """
        Remove a component from the internal list of components.

        :param component: A Discord Bot Engine Component
        :type component: Component
        """
        self._components.remove(component)

    def get_components(self) -> list[Component]:
        """
        Retrieve a read-only version of the internal list of components.

        :return: A list of Discord Bot Engine Components
        :rtype: list[Component]
        """
        return self._components.copy()

    def run(self, processes: bool = False, pool_size: int = 0) -> None:
        """
        Start the event loop by running all components using separate
        sub-threads or -processes.

        :param processes: Use subprocesses instead of threads, defaults to
        False
        :type processes: bool, optional
        :param pool_size: Specify the amount of processes that run at a time.
        Only used when `processes` is set to True. A value of 0 means that
        every component will run in its own process, defaults to 0.
        :type pool_size: int, optional
        """
        names = set()
        for comp in self._components:
            if comp.name not in names:
                names.add(comp.name)
            else:
                raise DuplicatedComponentNameError(
                    f"Name {comp.name} appears at least twice"
                )

        if not processes:
            for component in self._components:
                queue: Queue[Any] = Queue()
                thread = Thread(
                    target=component.run,
                    name=f"dbe-component-{component.name}",
                    args=(self, queue),
                    daemon=True,
                )
                self._components_threads_queues.append(
                    (component, thread, queue)
                )
                thread.start()
        else:
            if pool_size > 0:
                pool = ThreadPool(processes=pool_size)
                for component in self._components:
                    mp_queue: MPQueue[Any] = MPQueue()
                    pool.apply_async(func=component.run, args=(self, mp_queue))
                    self._components_threads_queues.append(
                        (component, pool, mp_queue)
                    )
            else:
                mp_queue = MPQueue()
                process = Process(
                    target=component.run,
                    name=f"dbe-component-{component.name}",
                    args=(self, mp_queue),
                    daemon=True
                )
                self._components_threads_queues.append(
                    (component, process, mp_queue)
                )
                process.start()

        self.loop()

    def loop(self) -> None:
        pass
