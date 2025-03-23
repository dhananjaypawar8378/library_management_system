from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register_admin(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect("register_admin")

        # Check if the email already exists (optional)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please use another email.")
            return redirect("register_admin")

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = True  # Make user an admin
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login_admin")

    return render(request, "register.html")


def login_admin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            messages.success(request, "Login successful! Welcome back.")
            return redirect("book_list")
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "login.html")

def logout_admin(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect("login_admin")

def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"],
            author=request.POST["author"],
            isbn=request.POST["isbn"],
            published_date=request.POST["published_date"]
        )
        return redirect("book_list")
    return render(request, "add_book.html")

def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.isbn = request.POST["isbn"]
        book.published_date = request.POST["published_date"]
        book.save()
        return redirect("book_list")
    return render(request, "update_book.html", {"book": book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "delete_book.html", {"book": book})

def base(request):
    return render(request, "base.html") 



def student_book_list(request):
    books = Book.objects.all()
    return render(request, "student_book_list.html", {"books": books})
