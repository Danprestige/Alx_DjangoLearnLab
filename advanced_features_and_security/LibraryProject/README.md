## Admin Integration

The Book model has been registered with Django admin.

- Columns displayed in list view: title, author, publication_year
- Sidebar filter: publication_year
- Searchable fields: title, author

How to Access:
1. Create superuser: python manage.py createsuperuser
2. Run server: python manage.py runserver
3. Go to: http://127.0.0.1:8000/admin/
