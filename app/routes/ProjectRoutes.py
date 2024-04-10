from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database_conn import get_db
from app.models.ProjectModel import Project
from app.schemas.ProjectSchema import ProjectRead
from app.services.ProjectServices import (
    get_project_by_id,
    get_all_projects as service_get_all_projects,
)

router = APIRouter(tags=["Project"])

@router.get("/projects/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    return get_project_by_id(db, project_id)

@router.get("/projects", response_model=List[ProjectRead])
def get_all_projects(db: Session = Depends(get_db)):
    return service_get_all_projects(db)


