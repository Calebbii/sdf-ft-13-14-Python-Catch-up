from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# ORM(Object Relational Mapping)
# Maps python objects to the db tables
# Maps Python classes to database tables, and objects to rows

# SQLalchemy - CRUD basics

# What is sqlalchemy
# SQLAlchemy is a powerful Python SQL toolkit and Object Relational Mapper (ORM) that allows developers to interact with relational databases like SQLite, PostgreSQL, MySQL, and others using Python code instead of raw SQL.

#  Why Use SQLAlchemy?
# ✅ Avoid writing raw SQL
# ✅ Cleaner, reusable code
# ✅ Supports multiple database engines
# ✅ Lets you define your DB schema using Python classes
# ✅ Handles relationships (foreign keys, joins) in an intuitive way

# Installing SQLalchemy
# pip install sqlalchemy

# Create the db engine
# Configure the session
# Define the table
# Creating the actual table
# CRUD Basics

# Create the db engine
engine = create_engine('sqlite:///students.db')

# Configure the session
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the table(students)
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key = True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    grade = Column(Integer)


# Creating the actual table
Base.metadata.create_all(engine)


student_one = Student(first_name="Joyrose", last_name="Kinuthia", grade=96)
student_two = Student(first_name="Ken", last_name="Ochieng", grade=99)

# Adding students to the db
# session.add(student_one)
# session.add(student_two)


# Adding multiple students at a go
session.add_all([student_two, student_one])


# Deleting students in the database
# session.delete(student_two)

# Fetching this student from the db before deleting
student_to_be_deleted = session.query(Student).filter_by(first_name="Ken", last_name="Ochieng").first()

if student_to_be_deleted:
    session.delete(student_to_be_deleted)
    session.commit()
    print(f"Deleted {student_to_be_deleted.first_name} {student_to_be_deleted.last_name}")
else:
    print("Student not found")


session.commit()