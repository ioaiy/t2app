# Django REST API

## Description
This project a REST API server supporting pagination, sorting, and filtering for the Transaction and Wallet models.

## Tech Stack
- Python 3.10
- Django 5.0.2
- Django REST Framework 3.14.0
- MySQL 8.0
- Docker and Docker Compose
- Code styling with Wemake-python-styleguide, Black, Isort

## Installation and Setup

### Requirements
- Docker and Docker Compose must be installed on your system.

### Project Setup
1. Clone the repository and navigate to the directory:
- `git clone https://github.com/ioaiy/t2app.git`
- `cd <project-directory>`
2. Launch the services using Docker Compose:
- `docker compose up -d --build`
3. Perform database migrations:
- `docker-compose exec web python manage.py migrate`
4. Grant database user privileges:
- `docker-compose exec -i db mysql -uroot -prootpassword -e "GRANT ALL PRIVILEGES ON ``test_%``.* TO 'myuser'@'%'; GRANT ALL PRIVILEGES ON ``mydatabase``.* TO 'myuser'@'%'; FLUSH PRIVILEGES;"`

### Run tests
- `docker-compose exec web python manage.py test t2test.apps.ledgers`
- `docker-compose exec web coverage run --source='.' manage.py test t2test.apps.ledgers`

## API Documentation
API documentation and usage details are available at `http://localhost:8010/docs/`.
