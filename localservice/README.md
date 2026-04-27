# LocalService Connect

A web platform connecting users with local service providers (plumbers, electricians, repair workers).

## Quick Setup

### 1. Install Python 3.10+
Make sure Python is installed: https://www.python.org/downloads/

### 2. Install Django
```bash
pip install -r requirements.txt
```

### 3. Initialize the project (migrations + demo data)
```bash
python setup_demo.py
```

### 4. Run the development server
```bash
python manage.py runserver
```

### 5. Open in browser
Visit: http://127.0.0.1:8000/

---

## Demo Login Accounts

| Role   | Username | Password |
|--------|----------|----------|
| User   | rohan    | pass123  |
| Worker | vikram   | pass123  |
| Admin  | admin    | admin123 |

> Admin panel is at `/admin-panel/` (login as `admin`)

---

## Project Structure

```
localservice/
├── manage.py
├── requirements.txt
├── setup_demo.py          # Run once to initialize
├── localservice/          # Django project config
│   ├── settings.py
│   └── urls.py
├── accounts/              # User & Worker registration/login
│   ├── models.py          # Profile model (role: user/worker)
│   ├── views.py
│   └── templates/
├── services/              # Core service request flow
│   ├── models.py          # ServiceRequest model
│   ├── views.py
│   └── templates/
├── adminpanel/            # Admin overview (staff only)
│   ├── views.py
│   └── templates/
└── templates/
    └── base.html          # Shared layout
```

## Workflow

1. User registers → submits a service request (type, description, location)
2. Request stored as **Pending**
3. Worker logs in → sees all pending requests → accepts or rejects
4. Accepted request assigned to that worker → status: **Accepted**
5. Worker marks job done → status: **Completed**
6. Admin can view everything at `/admin-panel/`

## Extending the project

- Add email notifications: use Django's `send_mail()` on status changes
- Add Google Maps: embed a Maps iframe using the location string
- Add ratings: create a `Review` model linked to completed `ServiceRequest`
- Deploy: use Railway, Render, or PythonAnywhere (all free tiers)
