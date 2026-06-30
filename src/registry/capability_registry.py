from __future__ import annotations

from src.database.models import (
    Capability,
    CapabilityStatus,
    CapabilityType,
)
from src.memory.manager import MemoryManager


class CapabilityRegistry:
    """
    Registers and discovers capabilities.
    """

    def __init__(self):
        self.memory = MemoryManager()

    def register_native(
        self,
        name: str,
        description: str,
        entrypoint: str,
    ):

        existing = self.memory.capabilities.get_by_name(name)

        if existing:
            return existing

        capability = Capability(
            name=name,
            description=description,
            capability_type=CapabilityType.NATIVE,
            status=CapabilityStatus.ACTIVE,
            entrypoint=entrypoint,
        )

        return self.memory.capabilities.add(capability)

    def get(self, name: str):
        return self.memory.capabilities.get_by_name(name)

    def list_capabilities(self):
        return self.memory.capabilities.list_all()
