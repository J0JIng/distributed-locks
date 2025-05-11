from abc import ABC, abstractmethod

class DistributedLock(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def getLock(self)-> bool:
        """Attempt to acquire the lock. Returns True if successful."""
        pass
    
    @abstractmethod
    def releaseLock(self)-> bool:
        """Release the lock. Returns True if successful."""
        pass


