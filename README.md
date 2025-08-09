# Task-4_Classera
Implement SQL Schema in Python ORM with FastAPI Endpoints
 Objective:
 Implement a Python backend using FastAPI and ORM from a given SQL schema (for LMS).
 Steps:
 1. Convert this SQL schema into SQLAlchemy models (ORM):
 users(id, name, email, role)
 courses(id, title, description)
 enrollments(id, user_id, course_id, status)
 assignments(id, course_id, title, due_date)
 submissions(id, assignment_id, user_id, file_url, grade)
 2. Set up a FastAPI project.
 3. Connect to PostgreSQL using SQLAlchemy.
 4. Create API endpoints for managing:
 Users: 
GET , 
POST , 
Courses: 
DELETE
 GET , 
POST , 
PUT
 Enrollments: 
POST a student into a course
 Assignments: create and list assignments for a course
 Submissions: submit and grade
 5. Use Pydantic for input validation.
 6. Use Alembic for DB migrations.
 7. Use 
.env file for DB config
