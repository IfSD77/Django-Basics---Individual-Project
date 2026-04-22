# Structural Portfolio UK

A professional catalog of structural engineering projects designed during my 8 years working in the UK.  
Developed as an individual project for the **SoftUni Django Basics Regular Exam**.

## Features

- **Project Catalog** with detailed information, images and construction data
- **Full CRUD functionality** for Projects (Create, Read, Update, Delete)
- **Dynamic filtering** by construction type and year
- **Project team** displayed through Many-to-Many relationship
- **Responsive design** built with Bootstrap 5
- **Custom 404 error page**
- **Read-only fields** in edit forms (Built In year and Construction Type)
- **Reusable template partials** for better code organization

## Technologies Used

- Django 5.2
- PostgreSQL
- Bootstrap 5 (via CDN)
- Pillow (for ImageField)
- Django Class-Based Views (CBVs)
- Template inheritance and reusable partials

## Database Design

- **3 Django apps**: `projects`, `designers`, `participations`
- **Models**:
  - `Project`
  - `ConstructionType`
  - `Designer`
  - `Participation` (Many-to-Many relationship between Project and Designer)
- Relationships: one ForeignKey + one Many-to-Many

## Local Setup
1. **Clone the repository:**
    - [git clone](https://github.com/IfSD77/Django-Basics---Individual-Project.git)
    - cd struct-portfolio-uk
2. **Create and activate virtual environment:**
    - python -m venv .venv
    - .venv\Scripts\activate
3. **Install dependencies:**
    - pip install -r requirements.txt
4. **Configure PostgreSQL in .env file:**
5. **Apply migrations:**
    - python manage.py makemigrations
    - python manage.py migrate
6. **Create superuser (optional, for admin):**
    - python manage.py createsuperuser
7. **Run the development server:**
    - python manage.py runserver
    - Open your browser at: http://127.0.0.1:8000/

## Project Structure

- `projects/` – Main models, forms, views and templates for projects
- `designers/` – Designer model and team management
- `participations/` – Many-to-Many relationship between projects and designers
- `templates/` – All HTML templates with base inheritance
- `staticfiles/` – Static files (CSS)

## Notes

- No authentication or user management (per exam rules)
- Complete CRUD operations for Projects
- All pages are reachable via the main navigation
- Project images are handled via Django's ImageField