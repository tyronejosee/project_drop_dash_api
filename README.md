<div align="center">
  <a href="https://github.com/tyronejosee/project_new_store#gh-light-mode-only" target="_blank">
    <img src="./.github/logo_light.svg" alt="logo-light" width="80">
  </a>
  <a href="https://github.com/tyronejosee/project_new_store#gh-dark-mode-only" target="_blank">
    <img src="./.github/logo_dark.svg" alt="logo-dark" width="80">
  </a>
</div>
<div align="center">
  <h1><strong>Drop Dash - API</strong></h1>
  <a href="#"><strong>Swagger UI</strong></a>
  🔸
  <a href="#"><strong>Redoc</strong></a>
</div>
<p align="center">
This API simulates a home delivery platform that allows users to search for and purchase products from local restaurants near their homes, place orders, and schedule deliveries. Similarly, restaurants can manage their menus, receive orders, and handle their meals through the platform. The API is inspired by platforms like Rappi, Uber Eats, PedidosYa, and Glovo.
<p>

<p align="center">
  <a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/python-3.11.9-3572A5" alt="python-version">
  </a>
  <a href="https://www.djangoproject.com/">
  <img src="https://img.shields.io/badge/django-5.0.4-092E20" alt="django-version">
  </a>
  <a href="https://www.django-rest-framework.org/">
  <img src="https://img.shields.io/badge/drf-3.15.1-A30000" alt="django-version">
  </a>
  <a href="https://www.docker.com/">
  <img src="https://img.shields.io/badge/docker-26.0.0-0db7ed" alt="docker-version">
  </a>
</p>

## ⚙️ Installation

Clone the repository.

```bash
git clone git@github.com:tyronejosee/project_drop_dash_api.git
```

Create a virtual environment (Optional).

```bash
python -m venv env
```

Activate the virtual environment (Optional).

```bash
env\Scripts\activate
```

Install all dependencies (Optional).

```bash
pip install -r requirements/local.txt
```

Create an environment variable file .env.

```bash
SECRET_KEY=""
EMAIL_BACKEND=""
EMAIL_HOST=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_PORT=""
EMAIL_USE_TLS=""
```

Docker run.

```bash
(env) docker compose -f docker-compose.dev.yml up
(env) docker compose -f docker-compose.dev.yml up --build
(env) docker compose -f docker-compose.dev.yml stop
(env) docker compose -f docker-compose.dev.yml logs -f
(env) docker compose -f docker-compose.dev.yml start
(env) docker compose -f docker-compose.dev.yml restart <service>
```

Perform database migrations.

```bash
(env) docker compose -f docker-compose.dev.yml exec web bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations*
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate <app_label> <migration_name>
(env) docker compose -f docker-compose.dev.yml exec web python manage.py showmigrations
```

> Note: Create the migrations in case Django skips any.

## 🚀 Usage

Create a superuser to access the entire site without restrictions.

```bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
```

Log in to `admin`:

```bash
http://127.0.0.1:8000/admin/
```

Access to Swagger o Redoc.

```bash
http://127.0.0.1:8000/api/schema/swagger/
http://127.0.0.1:8000/api/schema/redoc/
```

## 🚨 Important Notes

Check the creation of migrations before creating them.

```bash
(env) docker compose -f docker-compose.dev.yml exec web bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations users
(env) docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate
```

> Note: Checking migrations before their creation is necessary to avoid inconsistencies in user models.

## 💾 PostgreSQL

```bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py dumpdata > backup.json
(env) docker compose -f docker-compose.dev.yml exec web python manage.py loaddata
(env) docker compose -f docker-compose.dev.yml exec db psql -U postgres -d fandomhub_db
(dropdash_db=#) \dt
(dropdash_db=#) \d <table>
```

## 💾 Redis

```bash
(env) docker compose exec redis redis-cli
(127.0.0.1:6379) keys *
```

## ⚖️ License

This project is under the [Apache-2.0 license](https://github.com/tyronejosee/project_drop_dash_api/blob/main/LICENSE).
