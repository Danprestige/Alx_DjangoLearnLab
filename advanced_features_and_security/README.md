# Advanced Features and Security

## Custom Permissions

The Book model defines custom permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups

- Admins → All permissions
- Editors → can_view, can_create, can_edit
- Viewers → can_view only

## Setup

Run:
python manage.py makemigrations
python manage.py migrate
python manage.py setup_groups

Assign users to groups via admin panel.
