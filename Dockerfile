# 1. Base Image
FROM python:3.10-slim

# Set environment variables for non-interactive operations
ENV PYTHONUNBUFFERED 1

# 2. Create a dedicated group and non-root user
# Using UID 1001 which is in the recommended range (1000-20000) for CKV_CHOREO_1
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser -u 1001 appuser

# 3. Setup working directory and install dependencies
WORKDIR /usr/src/app

# Copy requirements file and install dependencies (leverages Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application files
# Note: These files are currently owned by 'root'
COPY . .

# 5. FIX: Change ownership of the entire working directory to the non-root user.
# This ensures 'appuser' has read/write/execute permissions on the app files.
RUN chown -R appuser:appuser /usr/src/app

# 6. Switch to the non-root user (Satisfies CKV_DOCKER_3 and CKV_CHOREO_1)
USER appuser

# 7. Define the command to run when the container starts
CMD ["python", "app.py"]