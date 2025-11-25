from datetime import datetime
from sqlalchemy import or_, not_, and_
from .models import Student
from .db import get_db


def create_student(first_name: str, last_name: str, birthdate: datetime, bio: str | None = None):
    student = Student(
        first_name=first_name,
        last_name=last_name,
        birthdate=birthdate,
        bio=bio
    )
    
    with get_db() as session:
        session.add(student)
        session.commit()

def get_students() -> list[Student]:
    with get_db() as session:
        students = session.query(Student).all()
    
    return students

def get_one_student(student_id: int) -> Student | None:
    with get_db() as session:
        student = session.query(Student).get(student_id)
    
    return student

def search_students_by_first_name(first_name: str) -> list[Student]:
    with get_db() as session:
        students = session.query(Student).filter(Student.first_name==first_name).all()
    
    return students

def search_students_by_name(name: str) -> list[Student]:
    with get_db() as session:
        students = session.query(Student).filter(
            or_(Student.first_name.like(f'%{name}%'), Student.last_name.like(f'%{name}%'))
        ).all()
    
    return students


