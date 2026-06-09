# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Make sure the app directory is in PYTHONPATH
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Command to run the application (this can be changed depending on how you want to run your agent)
CMD ["python", "-m", "src.graph"]
