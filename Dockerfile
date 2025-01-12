# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Gradio uses
EXPOSE 8001

CMD ["gunicorn","-c","config.py","main:app"]