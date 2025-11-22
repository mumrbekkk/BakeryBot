# 1. Base Image
FROM python:3.10-slim

# Create a group and a non-root user named 'appuser' with UID 1001
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser -u 1001 appuser

# ... (Installation, copying files, etc.)

# Set the working directory
WORKDIR /usr/src/app

# Copy application files
COPY . .

# 2. Switch to the non-root user (Fix for CKV_DOCKER_3)
USER appuser

# Define the command to run when the container starts
CMD ["python", "app.py"]