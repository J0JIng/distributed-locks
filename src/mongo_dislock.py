from src.base_dislock import DistributedLock

class MongoDistributedLock(DistributedLock):
    def __init__(self, name: str):
        self.name = name

    def getLock(self)-> bool:
        """Attempt to acquire the lock. Returns True if successful."""
        pass
    
    def releaseLock(self)-> bool:
        """Release the lock. Returns True if successful."""
        pass


