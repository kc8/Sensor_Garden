import abc


class Observer(metaclass=abc.ABCMeta):
    __metaclass_ = abc.ABCMeta
    
    @abc.abstractmethod
    def update(self, value):
        """ """
        pass

    @abc.abstractmethod
    def error(self):
        """What to do on error"""
        pass

    def __enter__(self):
        """For context manager"""
        return self

    # @abc.abstractmethod # Not ready for implementation
    def __exit__(self, exc_type, exc_val, exc_tb):
        """For context manager"""
        pass
