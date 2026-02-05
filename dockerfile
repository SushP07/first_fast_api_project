# Comment
# Instrunctions Command
#
# Frontend Dockerfile for React application
# Stage 1: build frontend
FROM node:18 AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./ 
RUN npm ci
COPY frontend/ .
RUN npm run build

# Backend Server Dockerfile for FastAPI application
#
# Using the official Python image from the Docker Hub similar to python version 3.14.2
FROM python:3.14.2-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the built frontend from the frontend-build stage
COPY --from=frontend-build /app/frontend/build /app/static

# Install PostgreSQL client and libpq-dev for PostgreSQL support
RUN apt-get update && apt-get install -y build-essential postgresql-client libpq-dev && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN python -m pip install -r requirements.txt

# Set environment variables variable for FastAPI Application
ENV FASTAPI_APP=main:app

# Add labels to the Docker image for metadata
LABEL "com.example.vendor" = "Sushi's Delight"
LABEL version="1.0"
LABEL description="A FastAPI application for Sushi's Delight restaurant."


# Expose the port the app will listen on
EXPOSE 5000

# Default DB host/port (can be overridden at runtime with -e)
ENV DB_HOST=host.docker.internal
ENV DB_PORT=5432

# Run the command to start the FastAPI application using Uvicorn when the container launches
# Bind to 0.0.0.0 so the container accepts external connections and use port 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

