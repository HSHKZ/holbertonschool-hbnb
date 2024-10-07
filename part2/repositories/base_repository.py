from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get_all(self):
        pass
