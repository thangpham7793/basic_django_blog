# Basic Django Blog

A basic Django blog with: 

- Tagging with [django-taggit](https://github.com/jazzband/django-taggit)
- Simple Insensitive Exact Text Search
- Basic Django RSS and XML Sitemaps

To run, make sure to have docker and docker-compose installed:

- In the root folder, add a .env with POSTGRES_PASSWORD and POSTGRES_USER matching the project's settings.py config
- Edit volume and other config values in docker-compose.yml
- docker-compose up -d --build
- [optional]: docker-compose restart [service-name] (in case of db connection error)

To use Django CLI from the container, prefix any command with "docker-compose exec [service-name] python manage.py" (or use an alias):

- docker-compose logs -f [service-name] (to see output from django app)
- [alias] makemmigrations
- [alias] migrate
- [alias] creatsuperuser (to create an admin user)
- [optional]: docker-compose exec [service-name] pipenv install [dependency]to install dep and update lock file)
- navigate to localhost:8000/admin to log in and add posts

Any changes made to the source code will be reflected. If not, simply restart or rebuild the container:
- docker-compose restart [service-name] | docker-compose up -d --build [service-name]

To enter the container:
- docker-compose exec [service-name] sh