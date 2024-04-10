from sqlalchemy.orm import Session
from app.models.ProjectModel import Project

def get_project_by_id(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def get_all_projects(db: Session):
    return db.query(Project).all()