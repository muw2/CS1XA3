# required
* python 2.7
* mysql >=5.6

# setUp

* git clone git@github.com:muw2/CS1XA3.git
> clone git project to local
* pip install virtualenv
> install virtual environment tools, if you have already installed it, skip it.
* virtualenv --no-site-packages cs_project3
> create virtual environment fro this project 
* source cs_project3/bin/activate
> get in virtual env
* pip install -r requirements.txt
> install requirements from freeze version
* python manage.py migrate
> create table for app
* python manage.py runserver
> run server 

# config


