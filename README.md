# Using Django and Google App Engine
A personal website in Django framework with Google App Engine. This is the source code for [lwinmoe.org](http://www.lwinmoe.org)

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

## To upload to Google App Engine
You will need to download and install [Google App Engine SDK](https://developers.google.com/appengine/downloads)

- Make sure you change the `application_name = 'lwinmoe'` to your application name in `src/sites/fabfile.py`
- Run `fab deploy` in `src/sites/my_site`
