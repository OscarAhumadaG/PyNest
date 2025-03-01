from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None  # Ensure `id` is truly optional
    username: str
    email: str

