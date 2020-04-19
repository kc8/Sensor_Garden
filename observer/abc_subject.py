from abc import ABCMeta
from observer.abc_observer import Observer


class Subject(metaclass=ABCMeta):
    __metaclass__ = ABCMeta
    _observers = set()

    def attach(self, observer):
        if isinstance(observer, Observer):
            self._observers |= {observer}
        else:
            raise TypeError("Observer not derivied from Abstract class Observer")

    def detatch(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()
