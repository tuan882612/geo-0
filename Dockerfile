# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# **Ensure the following steps run as root**

# Copy the entrypoint script and make it executable
COPY scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# switch to a non-root user after setting up permissions and changing ownership to non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

RUN chown -R appuser:appgroup /app

USER appuser

# Expose the port Gunicorn will run on
EXPOSE 8000

# Set the entrypoint script as the container's entrypoint
ENTRYPOINT ["/entrypoint.sh"]