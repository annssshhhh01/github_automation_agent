from __future__ import annotations

from typing import Optional

from sqlmodel import Session, select

from src.database.models import Capability


class CapabilityRepository:
    """
    Handles all database operations for capabilities.
    """

    def __init__(self, session: Session):
        self.session = session

    def add(self, capability: Capability) -> Capability:
        self.session.add(capability)
        self.session.commit()
        self.session.refresh(capability)
        return capability

    def get_by_name(self, name: str) -> Optional[Capability]:
        statement = select(Capability).where(Capability.name == name)
        return self.session.exec(statement).first()

    def list_all(self) -> list[Capability]:
        statement = select(Capability)
        return list(self.session.exec(statement))

    def update(self, capability: Capability):
        self.session.add(capability)
        self.session.commit()
        self.session.refresh(capability)

    def delete(self, capability: Capability):
        self.session.delete(capability)
        self.session.commit()
