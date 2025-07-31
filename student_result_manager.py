'''
Student Result Manager - Django Project
Tech Stack: Python, Django, SQLite, HTML, CSS, Bootstrap
'''

# ===========================
# STEP 1: Project Structure
# ===========================
# student_result_manager/
# ├── manage.py
# ├── result_app/
# │   ├── __init__.py
# │   ├── admin.py
# │   ├── apps.py
# │   ├── models.py
# │   ├── views.py
# │   ├── urls.py
# │   ├── templates/
# │   │   └── index.html
# │   └── static/
# ├── student_result_manager/
# │   ├── __init__.py
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py

# ===========================
# STEP 2: models.py
# ===========================
from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return self.name

# ===========================
# STEP 3: admin.py
# ===========================
from django.contrib import admin
from .models import Student

admin.site.register(Student)

# ===========================
# STEP 4: views.py
# ===========================
from django.shortcuts import render
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

# ===========================
# STEP 5: urls.py (in app)
# ===========================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# ===========================
# STEP 6: urls.py (in project folder)
# ===========================
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('result_app.urls')),
]

# ===========================
# STEP 7: index.html (basic template)
# ===========================
# Place this in result_app/templates/index.html
'''
<!DOCTYPE html>
<html>
<head>
    <title>Student Result Manager</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
<div class="container mt-4">
    <h2 class="mb-4">All Student Results</h2>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Roll No</th>
                <th>Name</th>
                <th>Branch</th>
                <th>Marks</th>
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.roll_no }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.branch }}</td>
                <td>{{ student.marks }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
</body>
</html>
'''

# ===========================
# STEP 8: README.md (description file)
# ===========================
'''
# Student Result Manager

A Django-based web application that allows you to manage student academic results.

## Features
- Add/view students and their marks
- Admin panel to add/edit/delete students
- Display all student records in a table

## Tech Stack
- Python
- Django
- HTML/CSS
- Bootstrap
- SQLite (default)

## Run the project
```bash
pip install django
django-admin startproject student_result_manager
cd student_result_manager
python manage.py startapp result_app
```
Copy the above files into respective folders and run:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then visit: `http://127.0.0.1:8000/`
'''

# End of Project 1 Code
