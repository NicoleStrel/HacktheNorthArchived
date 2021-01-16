# HacktheNorth

Hello!

## Enviornment Set up
- Clone GitHub repository locally `git clone [repo-link]`
- Setup a virtual environment:
  - Install: `pip install virtualenv`
  - Create: `virtualenv venv`
 - Activate the environment: `source venv/bin/activate` (keep it active when testing)
   - Use `deactivate` to close the env
 - Install the dependencies in the venv:
    - `pip install -r requirements.txt`

## Server Set Up
- Change directory: `cd hackthenorth`
- Run `python manage.py runserver`
- Website can be accessed at `127.0.0.1` or `localhost`

## Useful commands (model changes)
- `python manage.py makemigrations`
- `python manage.py showmigrations`
- `python manage.py migrate`

yay!
