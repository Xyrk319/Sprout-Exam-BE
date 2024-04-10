from pydantic import BaseModel


class ProjectRead(BaseModel):
    id: int
    name: str