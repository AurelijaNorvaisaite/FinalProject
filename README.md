# Expenses Registry
Powered by Django & Python

## General idea
This Registry WEB is created to help HR team in companies track daily/monthly or yearly expenses.

Cost type can be included by clicking "Išlaidų tipai"
![Alt text](registry/img/Type.png?raw=true "Type List")

The cost can be added by clicking "Išlaidos". Costs can be filtered by date and cost type.
![Alt text](registry/img/Filter1.png?raw=true "Filter List")

The monthly costs are shown by clicking on "Company cost control"
![Alt text](registry/img/MonthlyCosts.png?raw=true "Monthly costs")


## Install Docker

Before running the server, install docker (if choosing to use docker instead of SQLite).

Latest version(not necessary):
* [installing docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
* [installing docker compose](https://docs.docker.com/compose/install/)

Older version apt-get:
* [installing docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
* `$ sudo apt-get install docker-compose`

## Usefull Commands

* Install virtual environment<br />
`$ pip install pipenv`

* Run virtual environment<br />
`$ pipenv shell`

* Install pipfile, pipfile.lock, requirements.txt at once<br />
`$ pipenv install`

* Check if all requirements are installed<br />
`$ pip list`

* To start project you must make migrations<br />
`$ python (or python3) manage.py makemigrations`<br />
`$ python (or python3) manage.py migrate (will migrate all at once)`

* Create SuperUser (admin)<br />
`$ python manage.py createsuperuser`

* Run docker locally<br />
`$ docker-compose up -d`

* List running docker containers
`$ sudo docker ps`

![Alt text](registry/img/Container.png?raw=true "Container List")

* Run server<br />
`$ python manage.py runserver`
