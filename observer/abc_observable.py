"""Observable or also the Publisher or Subject method"""

from abc import ABCMeta
from observer.abc_observer import Observer
from observer.exceptions import FailedToRemoveObserver


class Observable(metaclass=ABCMeta):
    __metaclass__ = ABCMeta
    _observers = set()

    def add(self, observer):
        if isinstance(observer, Observer):
            self._observers |= {observer}
        else:
            raise TypeError("Observer not derivied from Abstract class Observer")

    def remove(self, observer):
        try:
            self._observers -= {observer}
        except:
            raise FailedToRemoveObserver("Failed to remove observer: {}".format(observer))

    def notify(self, value=None):
        """Notifies all observers of changes
        """
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()