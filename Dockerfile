FROM python:3.11-slim

# Create a non-root user
RUN useradd -m botuser

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER botuser

# Run the bot
CMD ["python", "main.py"]
