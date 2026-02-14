# LibraryProject - Advanced Features and Security

## Custom Permissions

The Book model defines the following custom permissions:

- can_view
- can_create
- can_edit
- can_delete

These permissions are added inside the Meta class of the Book model.

## Groups

The following groups are configured:

- Admins → All permissions
- Editors → can_view, can_create, can_edit
- Viewers → can_view only

## Setup Instructions

Run the following commands:

python manage.py makemigrations
python manage.py migrate
python manage.py setup_groups

Users can then be assigned to groups via the Django admin panel.


