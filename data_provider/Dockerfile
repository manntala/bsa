# Use official Python image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies, netcat, and curl
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev netcat-openbsd curl && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

CMD ["gunicorn", "data_provider.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
