# Stage 1: Builder
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---
# Stage 2: Final Image
FROM python:3.11-slim

# Choreo security requirement
ENV UID=10001
ENV GID=10001
RUN groupadd -g $GID nonroot \
    && useradd -u $UID -g nonroot -s /bin/bash nonroot

WORKDIR /app

# Copy installed dependencies and code
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

# Switch to the non-root user
USER nonroot

# Command to run the bot in polling mode
CMD ["python", "main.py"]