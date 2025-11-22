# 1. Base Image
FROM python:3.10-slim

# Set environment variables for non-interactive operations
ENV PYTHONUNBUFFERED 1

# 2. Create a dedicated group and non-root user
# We are creating a user 'appuser' with UID/GID 1001.
# This UID is within the scanner's required range of 1000-20000 (Fix for CKV_CHOREO_1).
RUN groupadd -r appuser -g 1001 && useradd --no-log-init -r -g appuser -u 1001 appuser

# 3. Setup working directory and install dependencies
WORKDIR /usr/src/app

# Copy requirements file and install dependencies (leverages Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application files
# The COPY operation is run as root, so the files are owned by root initially.
COPY . .

# 5. CRITICAL FIX: Change ownership of the directory to the non-root user (1001).
# This is mandatory so the non-root user can read and execute the application files.
# Using the numeric UID:GID (1001:1001) for maximum reliability across base images.
RUN chown -R 1001:1001 /usr/src/app

# 6. Switch to the non-root user's UID (Strict fix for CKV_CHOREO_1 scanner)
# We use the numeric ID '1001' here to explicitly satisfy the scanner's rule.
USER 1001

# 7. Define the command to run when the container starts
CMD ["python", "app.py"]