# UniversityHub

A simple Django application for managing departments and student registrations at a university. It allows administrators to create departments and students to register themselves with a selected department.

## Features

- View list of departments
- Students can register with first name, last name, email and choose a department
- Registration confirmation page
- Uses Django ModelForms for clean form handling

## Project Structure

```
academic_app/       # main Django app
    models.py       # Department and Student models
    forms.py        # StudentRegistrationForm
    views.py        # view functions for pages
    urls.py         # app-specific routes
    templates/      # HTML templates for each view
    static/         # CSS files

universityhub/      # project configuration
    settings.py     # Django settings
    urls.py         # root URL configuration

manage.py           # Django command-line utility
```

## Setup & Running

1. **Clone repository**
   ```bash
   git clone <repo-url> universityhub
   cd universityhub
   ```
2. **Create and activate virtualenv**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install django
   ```
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run development server**
   ```bash
   python manage.py runserver
   ```

Access the site at `http://127.0.0.1:8000/` and navigate to the student registration and departments pages.

## Usage

- Add departments through the Django admin or directly in code/migrations.
- Visit `/student_registration/` to register a student.
- Successful registrations redirect to `/registration_success/`.

## Notes

- The form uses `ModelForm` and custom widgets for Bootstrap-compatible styling.
- Departments are looked up by name; ensure names are unique.

## License

This project is provided for educational purposes. Feel free to adapt and extend it.
