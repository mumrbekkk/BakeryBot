# Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY main.py .
COPY handlers/ ./handlers/
COPY states/ ./states/
COPY utils/ ./utils/
COPY alembic/ ./alembic/
COPY alembic.ini .
COPY requirements.txt .
COPY core/ ./core/
COPY database/ ./database/
COPY helpers/ ./helpers/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "main.py"]

