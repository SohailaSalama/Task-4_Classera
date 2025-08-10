from pydantic import BaseModel
from datetime import date
from typing import Optional

# ===== Users =====
class UserBase(BaseModel):
    name: str
    email: str
    role: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True


# ===== Courses =====
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    class Config:
        orm_mode = True


# ===== Enrollments =====
class EnrollmentBase(BaseModel):
    user_id: int
    course_id: int
    status: str

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentResponse(EnrollmentBase):
    id: int
    class Config:
        orm_mode = True


# ===== Assignments =====
class AssignmentBase(BaseModel):
    course_id: int
    title: str
    due_date: Optional[date] = None

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentResponse(AssignmentBase):
    id: int
    class Config:
        orm_mode = True


# ===== Submissions =====
class SubmissionBase(BaseModel):
    assignment_id: int
    user_id: int
    file_url: Optional[str] = None
    grade: Optional[str] = None

class SubmissionCreate(SubmissionBase):
    pass

class SubmissionResponse(SubmissionBase):
    id: int
    class Config:
        orm_mode = True
class GradeSubmission(BaseModel):
    grade: str
