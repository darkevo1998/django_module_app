import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modular_project.settings')
django.setup()

from module_engine.models import Module

def init_product_module():
    # Create or update the product module
    module, created = Module.objects.get_or_create(
        name='product_module',
        defaults={
            'description': 'Product management module with CRUD operations and role-based access control',
            'version': '1.0.0',
            'is_installed': False
        }
    )
    
    if created:
        print("Product module created successfully")
    else:
        print("Product module already exists")

if __name__ == '__main__':
    init_product_module() 