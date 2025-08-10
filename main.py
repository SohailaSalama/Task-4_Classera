from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models, schemas

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "LMS FastAPI is running!"}

# ===== USERS =====
@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# ===== COURSES =====
@app.post("/courses/")
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses/")
def list_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db_course.title = course.title
    db_course.description = course.description
    db.commit()
    return db_course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(db_course)
    db.commit()
    return {"message": "Course deleted"}

# ===== ENROLLMENTS =====
@app.post("/enrollments/")
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    db_enrollment = models.Enrollment(
        user_id=enrollment.user_id, course_id=enrollment.course_id, status=enrollment.status
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

# ===== ASSIGNMENTS =====
@app.post("/assignments/")
def create_assignment(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    db_assignment = models.Assignment(
        course_id=assignment.course_id,
        title=assignment.title,
        due_date=assignment.due_date
    )
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

@app.get("/assignments/{course_id}")
def list_assignments(course_id: int, db: Session = Depends(get_db)):
    return db.query(models.Assignment).filter(models.Assignment.course_id == course_id).all()

# ===== SUBMISSIONS =====
@app.post("/submissions/")
def submit_assignment(submission: schemas.SubmissionCreate, db: Session = Depends(get_db)):
    db_submission = models.Submission(
        assignment_id=submission.assignment_id,
        user_id=submission.user_id,
        file_url=submission.file_url,
        grade=submission.grade
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

# ===== GRADE SUBMISSION =====
@app.put("/submissions/{submission_id}")
def grade_submission(submission_id: int, submission_data: schemas.GradeSubmission, db: Session = Depends(get_db)):
    submission = db.query(models.Submission).filter(models.Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    submission.grade = submission_data.grade
    db.commit()
    db.refresh(submission)
    return submission