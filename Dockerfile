FROM python:3.11.4

WORKDIR /app/

RUN pip install 'poetry==1.6.1'
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --only main

COPY . .

CMD chmod a+x scripts/*sh &&  \
    /app/scripts/run_migration.sh &&  \
    /app/scripts/run_gunicorn.sh
