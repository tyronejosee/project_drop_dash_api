FROM python:3.12.2-slim-bullseye
ENV PIP_DISABLE_PIP_VERSION_CKECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements/ /app/requirements/
RUN pip install -r requirements/local.txt
COPY . /app
CMD python manage.py runserver 0.0.0.0:8000
