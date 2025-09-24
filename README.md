# How to Run the Project

A simple Django project that renders templates.

## Steps to Run

```bash
git clone https://github.com/EduardGishyan1/django-task-1.git
cd django-task-1

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# (Optional) Create an admin user
python manage.py createsuperuser

# Start the development server
python manage.py runserver


Then open your browser at http://127.0.0.1:8000 to use the app.