from sqlmodel import SQLModel

class BaseModel(SQLModel):
    pass

# Import models so Alembic can discover them
from src.database.models import Capability, Execution, LearningMetric, KnowledgeBase, ToolVersion

metadata = SQLModel.metadata
