FROM python:3.7.4

WORKDIR /code

RUN apt-get -y update
RUN apt-get -y install netcat

RUN pip install --upgrade pip \
 && pip install poetry==1.0.4

COPY . .
COPY poetry.lock pyproject.toml wait_for_db.sh ./

RUN chmod +x "./wait_for_db.sh"
RUN poetry config virtualenvs.create false && poetry install $(test "$DJANGO_ENV" != "production" || echo "--no-dev") --no-interaction --no-ansi