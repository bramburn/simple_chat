# Use an official Python image as a base
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY poetry.lock requirements.txt ./

# Install the dependencies
RUN --rm -i poetry install --no-interaction

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000

# Run the command to start the development server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]