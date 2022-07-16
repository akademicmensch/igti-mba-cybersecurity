import string
from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts_id: List[int]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts_id: Optional[List[int]] = None


class GophishUser:
    def __init__(self, first_name, last_name, email, position):
        id: int
        self.first_name: string
        self.last_name: string
        self.email: string
        self.position: string

class GophishGroup:
    def __init__(self, group_name, targets):
        self.group_name: string
        self.targets: List(GophishUser)