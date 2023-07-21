# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev ffmpeg

# Set up a working directory inside the container
WORKDIR /app

# Copy the project files to the container's working directory
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot script
CMD ["python", "telegram_file_converter_bot.py"]
