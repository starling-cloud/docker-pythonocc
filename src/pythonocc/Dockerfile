# syntax=docker/dockerfile:1.4

# Base Image
# =============================================================================
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    liboce-foundation-dev \
    liboce-ocaf-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir wheel

# If you have a requirements.txt, you could add it and run pip install here:
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# Install pythonOCC
RUN pip install --no-cache-dir pythonocc-core

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
