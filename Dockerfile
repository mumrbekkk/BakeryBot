# Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY bot/ /app/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "main.py"]
