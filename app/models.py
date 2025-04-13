from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sql
import sqlalchemy.orm as orm
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


class User(UserMixin, db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(
        sql.String(64), index=True, unique=True
    )
    email: orm.Mapped[str] = orm.mapped_column(sql.String(64), index=True, unique=True)
    password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sql.String(265))

    # Virtual field
    posts: orm.WriteOnlyMapped["Post"] = orm.relationship(back_populates="author")

    # Setting hashing functionality for the password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}: {}>".format(self.id, self.username)


# flask_login requirement
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


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
