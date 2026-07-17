from app.database.base import Base
from app.models.analytics import Analytics
from app.models.automation import Automation, AutomationReplyType
from app.models.message import Message, MessageDirection, MessageStatus
from app.models.user import User
from app.schemas.analytics import AnalyticsCreate
from app.schemas.automation import AutomationCreate
from app.schemas.message import MessageCreate
from app.schemas.user import UserCreate


def test_database_metadata_registers_expected_tables() -> None:
    table_names = set(Base.metadata.tables.keys())

    assert {"users", "automations", "messages", "analytics"}.issubset(table_names)


def test_pydantic_schemas_validate_model_data() -> None:
    user = UserCreate(username="alice", full_name="Alice Example", is_active=True)
    automation = AutomationCreate(
        keyword="hello",
        reply_type=AutomationReplyType.TEXT,
        reply_text="Hi there!",
        is_enabled=True,
    )
    message = MessageCreate(
        instagram_user="user_123",
        message="Hello",
        reply="Hi",
        direction=MessageDirection.INCOMING,
        status=MessageStatus.PENDING,
    )
    analytics = AnalyticsCreate(keyword="hello", trigger_count=1)

    assert user.username == "alice"
    assert automation.reply_type == AutomationReplyType.TEXT
    assert message.direction == MessageDirection.INCOMING
    assert analytics.trigger_count == 1
