# Medical
# Getting Started


* clone the project in your local computer
```
$ git clone https://github.com/GouravSardana/Medical
```

## Prerequisites



```
- python3
- python3-pip
- virtualenvwrapper
- postgresql
- postgresql-contrib
- python-dev
- libpq-dev
- django
```

## Installing Prerequisites

```
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip virtualenvwrapper python-dev libpq-dev postgresql postgresql-contrib
```


## Creating Virtual Enviornment
* move to the cloned project directory
```
$ virtualenv -p /usr/bin/python3 env
```
activate the virtualenv
```
$ source env/bin/activate
```


## Installing and Running the project

```
$ cd Medical
```


```
$ python manage.py makemigrations
```
>if any prompt choose option 1
```
$ python manage.py migrate
```
> ignore some errors
```
$ python manage.py runserver
```
you will see something like This
```
Performing system checks...

System check identified no issues (0 silenced).
June 07, 2018 - 11:12:23
Django version 1.11.13, using settings 'Project_SLS.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Redirect at the link shown.

> use ctrl+c to stop the server and execute other command whenever needed.

## populating the data
Populate the data using admin panel

### creating superuser(admin)
```
$ python manage.py createsuperuser
```
> Fill the data asked in prompt


> run the server again
```
$ python manage.py runserver
```
> redirect to http://127.0.0.1:8000/admin.

> Login using the Email and Password you provided during creation of super user.


> populate some data of custom tags, Projects, softwares, activities.


> other data can be populated using the main app itself.
