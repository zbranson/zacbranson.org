# Using Django
A personal website in Django framework. This is the source code for [lwinmoe.org](http://www.lwinmoe.org)

## Requirements
- [Django version 1.5](https://www.djangoproject.com/)
- [Virtual Env](http://www.virtualenv.org/en/latest/)
- [Compass](http://compass-style.org/install/)

## How to run
- `cd src/sites`
- `virtualenv env`
- `. env/bin/activate`
- `pip install -r requirements.txt`
- `cd my_sites`
- `python manage.py syncdb`
- `python manage.py migrate`
- `compass compile`
- `python manage.py runserver`
