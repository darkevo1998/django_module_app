# Modular Django Project

This is a Django project that demonstrates a modular application architecture with a module engine and a sample product module.

## Features

- Module Engine for managing installable modules
- Product Module with CRUD operations
- Role-based access control (Manager, User, Public)
- Bootstrap-based responsive UI
- Form validation and confirmation dialogs

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Create user groups and assign permissions:
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from product_module.models import Product

# Create groups
manager_group = Group.objects.create(name='manager')
user_group = Group.objects.create(name='user')
public_group = Group.objects.create(name='public')

# Get content type for Product model
content_type = ContentType.objects.get_for_model(Product)

# Get all permissions for Product model
product_permissions = Permission.objects.filter(content_type=content_type)

# Assign permissions to groups
manager_group.permissions.set(product_permissions)  # CRUD
user_group.permissions.set(product_permissions.filter(codename__in=['add_product', 'change_product', 'view_product']))  # CRU
public_group.permissions.set(product_permissions.filter(codename='view_product'))  # R
```

6. Run the development server:
```bash
python manage.py runserver
```

## Access Credentials

- Superuser (Admin):
  - Username: admin
  - Password: admin123

- Manager User:
  - Username: manager
  - Password: manager123

- Regular User:
  - Username: user
  - Password: user123

## Usage

1. Access the module management page at `/module/`
2. Install the product module
3. Access the product management page at `/products/`
4. Create, read, update, and delete products based on your role permissions

## Project Structure

- `module_engine/`: Core module management functionality
- `product_module/`: Sample product management module
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS)
- `modular_project/`: Main project settings 