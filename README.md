![Logo of the project](https://raw.githubusercontent.com/jehna/readme-best-practices/master/sample-logo.png)

# Task Manager System

Simple task manager project which will help you organize your tasks in developing
This project uses django, django-orm, bootstrap5

### Check it out!
[Deploy on server](http://127.0.0.1:8000)

## Installation
Python3 must be already installed

Clone repository
```shell
git clone https://github.com/usrofgh/task_managment_system
cd task_managment_system/
python -m venv venv
source venv/Scripts/activate
pip install -r -requirements.txt
python manager.py migrate
python manage.py loaddata fixtures/*.json
python manage.py runserver
```
Script above clone repository, move there, create python venv and activate it.

After install all requirements, activate all migrations and load data for project

After run server

Go to http://127.0.0.1:8000

Credential data for login
```
User: admin
Password: admin
```


## Features

What's all the bells and whistles this project can perform?
* CRUD functional of tasks
* take tasks in work and cancel
* handy manage priority of tasks


## Demo
![ad task.png](demo%20screenshots%2Fad%20task.png)
![img_1.png](demo%20screenshots%2Fimg_1.png)
![img.png](img.png)
![img_1.png](img_1.png)