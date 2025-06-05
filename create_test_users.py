import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modular_project.settings')
django.setup()

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from product_module.models import Product

def create_test_users():
    # Create groups
    manager_group, _ = Group.objects.get_or_create(name='manager')
    user_group, _ = Group.objects.get_or_create(name='user')
    public_group, _ = Group.objects.get_or_create(name='public')

    # Get content type for Product model
    content_type = ContentType.objects.get_for_model(Product)

    # Get all permissions for Product model
    product_permissions = Permission.objects.filter(content_type=content_type)

    # Assign permissions to groups
    manager_group.permissions.set(product_permissions)  # CRUD
    user_group.permissions.set(product_permissions.filter(codename__in=['add_product', 'change_product', 'view_product']))  # CRU
    public_group.permissions.set(product_permissions.filter(codename='view_product'))  # R

    # Create test users
    users_data = [
        {
            'username': 'manager',
            'password': 'manager123',
            'email': 'manager@example.com',
            'groups': [manager_group]
        },
        {
            'username': 'user',
            'password': 'user123',
            'email': 'user@example.com',
            'groups': [user_group]
        },
        {
            'username': 'public',
            'password': 'public123',
            'email': 'public@example.com',
            'groups': [public_group]
        }
    ]

    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            email=user_data['email']
        )
        if created:
            user.set_password(user_data['password'])
            user.save()
            user.groups.set(user_data['groups'])
            print(f"Created user: {user_data['username']}")
        else:
            print(f"User already exists: {user_data['username']}")

if __name__ == '__main__':
    create_test_users() 