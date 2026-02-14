# Permissions and Groups Implementation

## Custom Permissions
The Book model defines:
- can_view
- can_create
- can_edit
- can_delete

## Groups Created
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → All permissions

## View Protection
Views are protected using Django's @permission_required decorator.

Example:
@permission_required('bookshelf.can_edit', raise_exception=True)

## Testing
Users were assigned to groups and tested to confirm that permission restrictions work correctly.
