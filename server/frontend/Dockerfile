# Dockerize the frontend
FROM python:3.10-slim-bullseye

WORKDIR /app/

# Install curl to slim image
RUN apt-get -y update && apt-get -y install curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root

COPY ./creddie_front/ /app/creddie_front/

COPY ./start.sh /app/

EXPOSE 8081

ENV PYTHONPATH=/app

CMD ["./start.sh"]