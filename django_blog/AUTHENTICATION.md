# Authentication System in django_blog

## Overview
This project uses Django's built-in authentication framework for user management. It includes:
- User registration
- Login and logout
- Profile editing

## Components
### Views
- `register_view`: Handles user registration with email
- `profile_view`: Allows users to edit profile details

### URLs
- `/register/` – registration
- `/login/` – login
- `/logout/` – logout
- `/profile/` – user profile

### Templates
Located in `blog/templates/registration/`

## Testing Instructions
1. Run `python manage.py runserver`
2. Visit each route and test form submissions
3. Ensure CSRF tokens are present and sessions persist after login
