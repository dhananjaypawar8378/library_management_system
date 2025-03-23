
# Library Management System

The Library Management System is a web-based application built with Django, designed to help manage library operations efficiently. It allows administrators to add, update, and delete books, as well as view the complete list of books available in the library. The system ensures ease of use for administrators to manage the library's collection while maintaining a clean and user-friendly interface.

## Installation

 

```bash
git clone https://github.com/dhananjaypawar8378/library_management_system.git
cd library_management
python3 -m venv myenv
source myenv/bin/activate  # For macOS/Linux
# or
myenv\Scripts\activate     # For Windows
pip install -r requirements.txt
python manage.py makemigrations  # Creates migrations for the app
python manage.py migrate        # Applies migrations to the database
python manage.py createsuperuser
python manage.py runserver


```
    
## Features
- Admin Panel: Secure login for admins to manage books.
- Book Management: Add, edit, and delete books in the system.
- Book List: View all available books in the library.
- Search and Filter: Easily search for books by title, author, or ISBN.
- Responsive Design: Optimized for both desktop and mobile devices.
## Prerequisites

- Python 
- pip (Python package installer)
- Django (should be installed via `requirements.txt`)
- Git