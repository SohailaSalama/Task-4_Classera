from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
    enrollments = relationship("Enrollment", back_populates="user")
    submissions = relationship("Submission", back_populates="user")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    enrollments = relationship("Enrollment", back_populates="course")
    assignments = relationship("Assignment", back_populates="course")

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    status = Column(String, nullable=False)
    user = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    title = Column(String, nullable=False)
    due_date = Column(Date)
    course = relationship("Course", back_populates="assignments")
    submissions = relationship("Submission", back_populates="assignment")

class Submission(Base):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    file_url = Column(String)
    grade = Column(String)
    assignment = relationship("Assignment", back_populates="submissions")
    user = relationship("User", back_populates="submissions")
