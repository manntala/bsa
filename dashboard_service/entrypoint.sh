# Use official Python image as base
FROM python:3.11-slim

# ... [other commands] ...

# Copy the wait-for-it script
COPY wait-for-it.sh /usr/local/bin/wait-for-it

# Copy entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# ... [install dependencies and other commands] ...

# Use the custom entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["gunicorn", "dashboard_service.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
