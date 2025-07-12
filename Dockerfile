# Dockerfile

FROM python:3.12-slim

# Install bash
RUN apt-get update && apt-get install -y bash

# Set working directory
WORKDIR /app

# Install pipenv and project dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy

# Copy Django code
COPY . .

# Create dummy user project folder
RUN mkdir -p /app/user_projects/project123

# Port for Daphne (Channels)
EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]
