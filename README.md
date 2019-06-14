# Django 2.X using Python3 in Glitch
---

## Starting your own project from scratch
You'll need to make a `glitch.json` file to tell your Glitch project what to install, and where to start running the application. In it, put:
```
{
  "install": "pip3 install -r requirements.txt --user",
  "start": "bash start.sh"
}
```
The `install` line tells Glitch to install any dependencies you put in your requirements.txt file. Go ahead and create one, and in it type:
```
Django==2.1.7
```
You can replace the version with whatever version of Django you'd like to develop with -- a newer one may be available.

The `start` line in `glitch.json` tells Glitch to launch `start.sh` as a shell script to start. 
Create a `start.sh` file and insert the following:
```
python3 manage.py runserver $PORT
```

Then create your Django project by running:
```
django-admin startproject yourprojectname .
refresh
```
Congrats! Your Django project should be up and running.
You should also hide your Django secret in your `.env`, and reference it in your settings.py:
```
SECRET_KEY = os.getenv('SECRET')
```

Follow the instructions below as well.

## Remixing this project
You need to allow Django to run at your Glitch URL. In your `settings.py`, edit this line with your own Glitch project name:
```
ALLOWED_HOSTS = ['your-project-name.glitch.me']
```
You'll also have to generate your SECRET in the `.env` that Django will use. Note that `.env` does not support certain characters such as `(` `)` `+` `=` or `&` in the secret without escaping.

Generating a new secret can be done from the console:
```
python3
>>> import random
>>> ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^*-_') for i in range(50))
