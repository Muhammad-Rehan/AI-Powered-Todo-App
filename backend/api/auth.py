from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Dict
from datetime import timedelta
import sys
import os

# Add the parent directory to the Python path for Vercel deployment
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.models.user import UserCreate
from auth.utils import create_access_token
from database import get_session
from config import settings
from services.user_service import UserService

router = APIRouter(tags=["Authentication"])

# -------------------------------
# Signup endpoint
# -------------------------------
@router.post("/signup", response_model=Dict[str, str])
def signup(user_data: UserCreate, session: Session = Depends(get_session)):
    """
    Register a new user and return access token.
    """
    user = UserService.create_user(session, user_data)

    access_token_expires = timedelta(
        minutes=settings.jwt_access_token_expire_minutes
    )
    access_token = create_access_token(
        data={"sub": str(user.user_id)},
        expires_delta=access_token_expires,
    )

    return {
        "user_id": str(user.user_id),
        "email": user.email,
        "token": access_token,
    }


import logging

# Configure logger
logger = logging.getLogger(__name__)

# -------------------------------
# Signin endpoint
# -------------------------------
@router.post("/signin", response_model=Dict[str, str])
def signin(user_data: UserCreate, session: Session = Depends(get_session)):
    """
    Authenticate a user and return JWT token.
    """
    try:
        logger.info(f"Attempting to sign in user: {user_data.email}")
        user = UserService.authenticate_user(
            session,
            user_data.email,
            user_data.password,
        )

        if not user:
            logger.warning(f"Failed authentication for user: {user_data.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )

        logger.info(f"User authenticated: {user_data.email}")
        access_token_expires = timedelta(
            minutes=settings.jwt_access_token_expire_minutes
        )
        access_token = create_access_token(
            data={"sub": str(user.user_id)},
            expires_delta=access_token_expires,
        )

        logger.info(f"Access token created for user: {user_data.email}")
        return {
            "user_id": str(user.user_id),
            "email": user.email,
            "token": access_token,
        }
    except Exception as e:
        logger.error(f"An unexpected error occurred during signin for user {user_data.email}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal server error occurred."
        )
