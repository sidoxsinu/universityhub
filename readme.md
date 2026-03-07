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
3. **Install dependencies from `requirements.txt`**
   ```bash
   pip install -r requirements.txt
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

Access the site at `http://127.0.0.1:8000/` (development) or deployed at [https://university-hub-dfru.onrender.com/](https://university-hub-dfru.onrender.com/). Navigate to the student registration and departments pages.

## Deployment

For production deployment (e.g., on Render):

1. Install additional dependencies:
   ```bash
   pip install whitenoise
   ```

2. Update `universityhub/settings.py`:
   - Set `DEBUG = False`
   - Add your deployment domain to `ALLOWED_HOSTS`
   - Add your domain with https to `CSRF_TRUSTED_ORIGINS`
   - Add `'whitenoise'` to `INSTALLED_APPS`
   - Add `'whitenoise.middleware.WhiteNoiseMiddleware'` to `MIDDLEWARE` after `SecurityMiddleware`

3. Run collectstatic:
   ```bash
   python manage.py collectstatic
   ```

4. Deploy to your platform (e.g., Render, Heroku)

## Usage

- Add departments through the Django admin or directly in code/migrations.
- Visit `/student_registration/` to register a student.
- Successful registrations redirect to `/registration_success/`.

## Notes

- The form uses `ModelForm` and custom widgets for Bootstrap-compatible styling.
- Departments are looked up by name; ensure names are unique.

## License

This project is provided for educational purposes. Feel free to adapt and extend it.
