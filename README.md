# Django_Book_Outlet

## Learning how relationships work in Django

In this project, you will see examples of One-to-many, One-to-one, and Many-to-many releationships.

This is based on an example of a Book store outlet.

Models:
Author - An author may have a single address (one-to-one) & many books (one-to-many)
Book - A book may have a single author (One-to-Many) and many books can be published in many countries (many to many)
Country - A book can be published in more than one country and a country may have more than one book published (many-to-many)
Address - An author may have a single address (one-to-one)

# How to

Using Python3, type in command line:
python3 manage.py runserver

# Admin Panel

Available at localhost:8000/admin
