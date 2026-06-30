from sqlmodel import Session

from src.database.session import engine
from src.memory.repository import CapabilityRepository


class MemoryManager:
    """
    Entry point to the persistent memory layer.
    """

    def __init__(self):
        self.session = Session(engine)
        self.capabilities = CapabilityRepository(self.session)

    def close(self):
        self.session.close()
