from typing import Optional
from datetime import datetime, timezone
import sqlalchemy as sql
import sqlalchemy.orm as orm

from app import db


class User(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(
        sql.String(64), index=True, unique=True
    )
    email: orm.Mapped[str] = orm.mapped_column(sql.String(64), index=True, unique=True)
    password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sql.String(265))

    # Virtual field
    posts: orm.WriteOnlyMapped["Post"] = orm.relationship(back_populates="author")

    def __repr__(self):
        return "<User {}: {}>".format(self.id, self.username)


class Post(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    body: orm.Mapped[str] = orm.mapped_column(sql.String(140))
    timestamp: orm.Mapped[datetime] = orm.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    user_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(User.id), index=True)
    # Virtual field
    author: orm.Mapped[User] = orm.relationship(back_populates="posts")

    def __repr__(self):
        return "<Post {}: {}>".format(self.id, self.body)
