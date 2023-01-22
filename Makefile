PYTHON_EXE?=python3
MANAGE=venv/bin/python manage.py
ACTIVATE?=. venv/bin/activate;
GET_SECRET_KEY=`base64 /dev/urandom | head -c50`
ENV_FILE=.env

# Default Django Port
PORT = 8000

virtualenv:
	@echo "-> Getting Essential Build Files"
	@sudo apt-get install python3-venv
	@echo "-> Making Virtual Environment"
	@${PYTHON_EXE} -m venv ./venv

genkey: virtualenv
	@echo "-> Generating Secret key"
	@if test -f ${ENV_FILE}; then echo ".env file exists already"; true; fi
	@mkdir -p $(shell dirname ${ENV_FILE}) && touch ${ENV_FILE}
	@echo SECRET_KEY=\"${GET_SECRET_KEY}\" > ${ENV_FILE}
	@cat etc/env.txt >> .env

install: genkey
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip install -r requirements.txt

dev: genkey
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip install -r dev.txt

project: dev
	@echo -n "-> Enter Project Name: ";\
	read PROJECT; \
	${ACTIVATE} django-admin startproject $${PROJECT} .


migrate:
	@echo "-> Apply database migrations"
	${MANAGE} makemigrations
	${MANAGE} migrate

run:
	${MANAGE} runserver ${PORT}

flush:
	@echo "-> Flushing Database"
	${MANAGE} flush

format:
	@echo "-> Run isort imports ordering validation"
	@${ACTIVATE} isort --profile black --gitignore .
	@echo "-> Run black validation"
	@${ACTIVATE} black --line-length 120 .

test:
	@${MANAGE} test

check: test
	@echo "-> Run black validation"
	@${ACTIVATE} black --check .

coverage: 
	@echo "-> Generating coverage report"
	@${ACTIVATE} coverage run --source='.' manage.py test
	@${ACTIVATE} coverage report
	@${ACTIVATE} coverage html
