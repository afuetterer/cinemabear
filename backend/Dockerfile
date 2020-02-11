FROM python:3.8.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install OS dependencies
RUN apk update \
    && apk add git build-base \
    && apk add bash \
    && apk add postgresql-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

# Install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system

# Copy project
COPY ./ ./