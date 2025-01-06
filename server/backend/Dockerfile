# Dockerize the backend
FROM python:3.10

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root

COPY ./creddie/ /app/creddie/

COPY ./alembic/ /app/alembic/

COPY ./alembic.ini ./prestart.sh ./start.sh /app/

EXPOSE 8080

ENV PYTHONPATH=/app

CMD ["./start.sh"]