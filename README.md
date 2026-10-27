# FUTURE_FS_02 — LeadFlow CRM

A responsive Client Lead Management System built for Future Interns Full Stack Web Development Task 2.

## Features
- Admin login using Django authentication and password hashing
- Dashboard metrics for total, new, contacted, and converted leads
- Create, read, update, and delete lead records
- Search by client name, email, or company; filter by status
- Lead source, company, phone, email, and context fields
- Activity notes attached to individual leads
- Schedule follow-ups and mark them complete
- Django admin interface for managing records
- SQLite database for quick local setup
- Responsive dashboard and detail pages
- CSRF protection on POST forms and login-required views

## Requirements
- Python 3.10 or newer
- pip

## Run locally (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and sign in with the superuser username/password you created. The first registered admin is created locally by you; no credentials are hard-coded in this repository.

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate again.

## Routes
- `/` — lead dashboard (login required)
- `/login/` — sign in
- `/leads/create/` — create a lead
- `/leads/<id>/` — lead profile, notes, follow-ups
- `/admin/` — Django admin (superuser required)

## Suggested manual test checklist
1. Log in with the superuser account.
2. Create a lead with valid name and email.
3. Search for the lead by name and filter by status.
4. Edit the lead and change its status to Contacted, then Converted.
5. Open its profile, add a note, and schedule a follow-up.
6. Mark the follow-up complete.
7. Delete a test lead and confirm it disappears.
8. Sign out and confirm dashboard redirects to login.

## GitHub submission
Create a **public** repository named `FUTURE_FS_02`. From inside this folder:
```powershell
git init
git add .
git commit -m "Build LeadFlow client lead management CRM"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/FUTURE_FS_02.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username. Do not commit passwords, secret keys, virtual environments, or a production database.

## Production notes
This is a local-development submission starter, not a hardened production deployment. Before public deployment, set a strong `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=False`, configure `ALLOWED_HOSTS`, HTTPS/cookie settings, static-file serving, database backups, and deployment-specific security settings. The sample settings are intentionally configured for local development.
