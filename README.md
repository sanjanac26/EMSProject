# Employee Management System

A Django-based Employee Management System with login authentication, search, and pagination.

## Features
- Secure login authentication (Django `LoginRequiredMixin` on all views)
- Add, edit, delete employee records
- Search employees by name, department, or ID
- Paginated employee list (20 per page)
- Dashboard showing total employee count

## Tech Stack
**Backend:** Python, Django, SQLite (dev) / PostgreSQL (production)
**Frontend:** HTML5, CSS3, JavaScript, Bootstrap

## Live Demo
<!-- Add your deployed link here once hosted -->
<!-- Example: https://ems-project.onrender.com -->

## Getting Started

### Prerequisites
- Python 3.10+

### Setup
```bash
git clone https://github.com/sanjanac26/EMSProject.git
cd EMSProject

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Create a .env file (see .env.example) and set your SECRET_KEY

python manage.py migrate
python manage.py createsuperuser   # create a login account
python manage.py runserver
```
Visit `http://127.0.0.1:8000/`

## Project Structure
```
EMSProject/
├── EMSProject/       # Django project settings
├── emsapp/           # Main app (models, views, templates)
├── manage.py
└── requirements.txt
```

## Author
**Sanjana Chavan**
[GitHub](https://github.com/sanjanac26)
