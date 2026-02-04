# Comment
# Instrunctions Command

# Using the official Python image from the Docker Hub similar to python version 3.14.2
FROM python:3.14.2-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

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


# Run the command to start the FastAPI application using Uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

