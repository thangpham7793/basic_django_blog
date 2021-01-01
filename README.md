# Basic Django Blog

A basic Django blog with: 

- Tagging with [django-taggit](https://github.com/jazzband/django-taggit)
- Simple Insensitive Exact Text Search
- Basic Django RSS and XML Sitemaps

To run, make sure to have pipenv, docker, and docker-compose installed:

- In the root folder, add a .env with POSTGRES_PASSWORD and POSTGRES_USER matching the project's settings.py config
- docker-compose up -d --build
- docker-compose logs -f web (to see output from django app)
- docker-compose exec python manage.py makemigrations
- docker-compose exec python manage.py migrate
- [optional]: docker-compose restart web (in case of db connection error)