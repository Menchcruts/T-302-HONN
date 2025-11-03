# syntax=docker/dockerfile:1
FROM python:3.12.11-slim-trixie

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .