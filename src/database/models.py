from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel


# ----------------------------
# ENUMS
# ----------------------------

class CapabilityType(str, Enum):
    NATIVE = "native"
    SYNTHESIZED = "synthesized"


class CapabilityStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    FAILED = "failed"
    DEPRECATED = "deprecated"


# ----------------------------
# CAPABILITY REGISTRY
# ----------------------------

class Capability(SQLModel, table=True):
    __tablename__ = "capabilities"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    name: str = Field(index=True, unique=True)

    description: str

    capability_type: CapabilityType

    status: CapabilityStatus = CapabilityStatus.ACTIVE

    entrypoint: str

    version: int = 1

    confidence: float = 1.0

    success_rate: float = 1.0

    times_used: int = 0

    average_execution_time: float = 0.0

    required_permissions: list = Field(
        default_factory=list,
        sa_column=Column(JSONB)
    )

    constraints: list = Field(
        default_factory=list,
        sa_column=Column(JSONB)
    )

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)

# ----------------------------
# MEMORY & EXECUTION
# ----------------------------

class Execution(SQLModel, table=True):

    __tablename__ = "execution_memory"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    instruction: str

    execution_plan: dict = Field(
        sa_column=Column(JSONB)
    )

    execution_report: dict = Field(
        sa_column=Column(JSONB)
    )

    success: bool

    execution_time: float

    api_calls: int

    learned_constraints: list = Field(
        default_factory=list,
        sa_column=Column(JSONB)
    )

    created_at: datetime = Field(default_factory=datetime.utcnow)


class LearningMetric(SQLModel, table=True):

    __tablename__ = "learning_metrics"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    instruction_pattern: str

    average_execution_time: float = 0

    average_api_calls: float = 0

    success_rate: float = 1.0

    optimized_plan: dict = Field(
        sa_column=Column(JSONB)
    )

    updated_at: datetime = Field(default_factory=datetime.utcnow)


class KnowledgeBase(SQLModel, table=True):

    __tablename__ = "knowledge_base"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    category: str

    observation: str

    confidence: float = 1.0

    source_execution: Optional[UUID] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)


class ToolVersion(SQLModel, table=True):

    __tablename__ = "tool_versions"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    capability_id: UUID

    version: int

    entrypoint: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
