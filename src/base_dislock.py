from abc import ABC, abstractmethod
from typing import Optional
import hashlib
import base64

class DistributedLock(ABC):
    def __init__(self, name: str):
        """Abstract class for distributed locks"""
        self.name = name
        self.hash = self.base64_sha256_hash(self.name)
        self.lock_acquired = False

    @abstractmethod
    def getLock(self) -> bool:
        pass

    @abstractmethod
    def releaseLock(self) -> bool:
        pass

    def base64_sha256_hash(self, input_string: str):
        """
        Returns a base64-encoded SHA-256 hash of the input string.
        
        Args:
            input_string (str): Input string to hash.
            
        Returns:
            str: Base64-encoded SHA-256 hash of the input string.
        """
        hash_bytes = hashlib.sha256(input_string.encode('utf-8')).digest()
        return base64.b64encode(hash_bytes).decode('utf-8')
