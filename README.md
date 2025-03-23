Library Management System

This is a Library Management System built with Django. It allows the management of books, including adding, editing, and deleting book entries. The system has functionality for both admins (to manage the library) and students (to view available books).

Features

Admin Panel:
Add, Edit, Delete books.
Manage users and permissions.
Student Panel:
View all available books in the library.
Authentication:
Admin login to access the library management features.
No login required for students.

Project Structure

library_management_system/
│
├── library_management/        # Main Django app
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, JS, images)
│   ├── templates/             # HTML Templates
│   ├── admin.py               # Admin configuration
│   ├── models.py              # Database models
│   ├── views.py               # Views for the app
│   ├── urls.py                # URL configurations
│   └── ...
│
├── manage.py                  # Django's command-line utility
├── requirements.txt           # Python dependencies
└── README.md                  # This file


Admin role: Only authorized users with admin credentials can add, edit, or delete books.
Student role: Students can only view the list of available books without needing to log in.
Setup Instructions

1. Clone the repository:
git clone https://github.com/dhananjaypawar8378/library_management_system.git
cd library_management_system
2. Set up a Python virtual environment:
python3 -m venv myenv
source myenv/bin/activate  # For macOS/Linux
myenv\Scripts\activate     # For Windows
3. Install required dependencies:
pip install -r requirements.txt
4. Set up the database:
python manage.py migrate
5. Create a superuser to access the admin panel:
python manage.py createsuperuser
6. Run the development server:
python manage.py runserver
Now, open http://127.0.0.1:8000 in your browser.

