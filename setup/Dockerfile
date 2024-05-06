FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile
COPY Pipfile.lock

# Install dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy --dev

COPY /app ./app
COPY /setup ./setup
COPY /migrations ./migrations
COPY /models ./models
COPY /settings ./settings
COPY main.py .
COPY Makefile .
COPY alembic.ini .
COPY setup/wait_for_db.py ./

RUN chmod a+x setup/entrypoint.sh
RUN chmod a+x /app/setup/wait_for_db.py