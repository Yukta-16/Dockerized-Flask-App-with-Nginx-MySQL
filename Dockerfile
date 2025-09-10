# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

# Run the app
CMD ["python", "app.py"]
