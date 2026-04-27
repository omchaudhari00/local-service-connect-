#!/usr/bin/env python3
"""
Run this script once after setting up the project to:
- Apply migrations
- Create a superuser (admin)
- Create sample data for testing
"""
import os, sys, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'localservice.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile
from services.models import ServiceRequest

print("Running migrations...")
from django.core.management import call_command
call_command('migrate', '--run-syncdb', verbosity=0)

print("Creating admin superuser...")
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    Profile.objects.create(user=admin, role='user', city='Ahmedabad')
    print("  admin / admin123")

print("Creating sample user...")
if not User.objects.filter(username='rohan').exists():
    user = User.objects.create_user('rohan', password='pass123', first_name='Rohan', last_name='Mehta')
    Profile.objects.create(user=user, role='user', city='Ahmedabad', phone='9876543210')
    print("  rohan / pass123")

print("Creating sample worker...")
if not User.objects.filter(username='vikram').exists():
    worker = User.objects.create_user('vikram', password='pass123', first_name='Vikram', last_name='Shah')
    Profile.objects.create(user=worker, role='worker', city='Ahmedabad', skill='Plumbing')
    print("  vikram / pass123")

print("Creating sample service requests...")
rohan = User.objects.get(username='rohan')
vikram = User.objects.get(username='vikram')
if ServiceRequest.objects.count() == 0:
    ServiceRequest.objects.create(
        user=rohan, service_type='Plumbing',
        description='Kitchen sink pipe is leaking near the drain.',
        location='Satellite, Ahmedabad', status='Accepted', worker=vikram
    )
    ServiceRequest.objects.create(
        user=rohan, service_type='Electrical',
        description='Main switchboard trips frequently.',
        location='Navrangpura, Ahmedabad', status='Pending'
    )
    ServiceRequest.objects.create(
        user=rohan, service_type='Hardware Repair',
        description='Laptop screen hinge broken, needs replacement.',
        location='Bopal, Ahmedabad', status='Completed', worker=vikram
    )

print("\nDone! Run the server with:")
print("  python manage.py runserver")
print("\nThen open: http://127.0.0.1:8000/")
print("\nLogin accounts:")
print("  User:   rohan / pass123")
print("  Worker: vikram / pass123")
print("  Admin:  admin / admin123  (also visit /admin-panel/ when logged in as admin)")
