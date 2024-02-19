import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, relationship

from src.attraction.models import Attraction
from src.db.database import Base
from src.threads.models import Comment, Review


class Media(Base):
    __tablename__ = "media"

    id: Mapped[uuid.UUID] = Column(
        UUID(),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    bucket_name: Mapped[str] = Column(String, index=True)
    file_name: Mapped[str] = Column(String)
    file_type: Mapped[str] = Column(String)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    attraction_id: Mapped[int] = Column(Integer, ForeignKey("attractions.id"))
    review_id: Mapped[uuid.UUID] = Column(UUID(as_uuid=True), ForeignKey("reviews.id"))
    comment_id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True), ForeignKey("comments.id")
    )

    attraction: Mapped[Attraction] = relationship("Attraction", back_populates="media")
    comment: Mapped[Comment] = relationship("Comment", back_populates="media")
    review: Mapped[Review] = relationship("Review", back_populates="media")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
