from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.crud_user import get_user_by_email
from app.deps import get_db

router = APIRouter(
    prefix="/users", tags=["Users"],
)


# @router.get("/" response_model=ListUsers)
# def list_users(search_query: Optional[str] = None, limit: Optional[int] = 100):
#     res = USERS
#     if search_query:
#         res = filter(lambda u: search_query.lower() in u["username"].lower(), USERS)
#     return {"user_list": list(res)[:limit]}

@router.get("/{email}")
def get_user(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email {email} not found."
        )

# @router.post("/users/")
# def create_user(user_data: CreateUser):
#     hashed_password = get_password_hash(user_data.password)
#     user = user_data.dict()
#     user["password"] = hashed_password
#     user = User(**user)
#     USERS.append(user.dict())
#     return user.dict()
#
#
# @router.get("/users/{user_id}", response_model=User)
# def get_user(user_id: uuid.UUID):
#     user = get_user_by_id(user_id)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with id {user_id} not found."
#         )
#     return user
