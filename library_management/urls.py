from django.contrib import admin
from django.urls import path
from . import views

from .views import register_admin, login_admin, logout_admin, book_list, add_book,update_book, delete_book

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.base, name="base"),
    path("register/", register_admin, name="register_admin"),
     path("login/", login_admin, name="login_admin"),
    path("logout/", logout_admin, name="logout_admin"), 
    path("books/add/", add_book, name="add_book"),
     path("books/", book_list, name="book_list"),  
    path("books/update/<int:book_id>/", update_book, name="update_book"),
    path("books/delete/<int:book_id>/", delete_book, name="delete_book"),
     path("student/books/", views.student_book_list, name="student_book_list"),
    
]
