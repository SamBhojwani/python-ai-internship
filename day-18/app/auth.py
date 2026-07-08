"""
auth.py
-------
Business logic for user registration and login.
"""

from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserRegister
from app.security import hash_password, verify_password


def get_user_by_username(db: Session, username: str) -> User | None:
    """Return a user by username or None if not found."""
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    """Return a user by email or None if not found."""
    return db.query(User).filter(User.email == email).first()


def register_user(db: Session, data: UserRegister) -> User:
    """Register a new user with a hashed password."""
    hashed = hash_password(data.password)
    user = User(
        username=data.username,
        email=data.email,
        hashed_password=hashed,
        role=data.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, username: str, password: str) -> User | None:
    """Verify username and password. Returns user if valid, None if not."""
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user