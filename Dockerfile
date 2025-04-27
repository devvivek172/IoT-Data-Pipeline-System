# Use an official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables if needed (optional)
ENV PYTHONUNBUFFERED=1

# Run the main application
CMD ["python", "src/main.py"]
