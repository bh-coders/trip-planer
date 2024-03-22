import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, relationship

from src.db.database import Base
from src.users.models import User


class Review(Base):
    __tablename__ = "reviews"
    id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    user_id: Mapped[uuid.UUID] = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    attraction_id: Mapped[int] = Column(Integer, ForeignKey("attractions.id"))
    rating: Mapped[int] = Column(Integer)
    price: Mapped[int] = Column(Integer)
    time_spent: Mapped[int] = Column(Integer)
    title: Mapped[str] = Column(String(255))
    description: Mapped[str] = Column(Text)

    user: Mapped[User] = relationship("User")
    attraction = relationship("Attraction")
    comments = relationship(
        "Comment",
        back_populates="review",
        cascade="all, delete-orphan",
        passive_deletes=True,
        order_by="Comment.created_at.asc()",
    )
    media = relationship("Media", back_populates="review", cascade="all, delete-orphan")

    def as_dict(self):
        review_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        review_dict["comments"] = [comment.as_dict() for comment in self.comments]
        review_dict["media"] = [media.as_dict() for media in self.media]

        return review_dict


class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[uuid.UUID] = Column(
        UUID,
        primary_key=True,
        default=uuid.uuid4,
    )
    review_id: Mapped[uuid.UUID] = Column(UUID, ForeignKey("reviews.id"))
    user_id: Mapped[uuid.UUID] = Column(UUID, ForeignKey("users.id"))
    content: Mapped[str] = Column(Text)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)

    review = relationship("Review", back_populates="comments")
    user: Mapped[User] = relationship("User")
    media = relationship(
        "Media", back_populates="comment", cascade="all, delete-orphan"
    )

    def as_dict(self):
        comment_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        comment_dict["media"] = [media.as_dict() for media in self.media]

        return comment_dict
