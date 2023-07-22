# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir Flask

# Expose the port that the Flask app will run on
EXPOSE 5000

# Define the command to run the Flask app when the container starts
CMD ["python", "app.py"]
