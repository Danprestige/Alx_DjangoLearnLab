# LibraryProject/bookshelf/management/commands/setup_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Create groups and assign permissions for Book model"

    def handle(self, *args, **kwargs):
        # Get the Book model
        Book = apps.get_model('bookshelf', 'Book')

        # Get all permissions for the Book model
        permissions = Permission.objects.filter(content_type__app_label='bookshelf', content_type__model='book')

        # Define which permissions each group should have
        group_permissions = {
            "Admins": permissions,  # All permissions
            "Editors": permissions.filter(codename__in=['can_create', 'can_edit', 'can_view']),
            "Viewers": permissions.filter(codename__in=['can_view']),
        }

        # Create groups and assign permissions
        for group_name, perms in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set(perms)
            group.save()
            self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" created/updated with permissions.'))
