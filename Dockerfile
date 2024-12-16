# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install the dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Expose the necessary port (for a web application, typically 8000)
EXPOSE 8000

# Command to run your application (replace with your app's command)
CMD ["python", "app.py"]
