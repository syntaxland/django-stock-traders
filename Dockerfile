# Using an official python runtime as the base image
FROM python:3.9-alpine 
# Set the working directory in the container
WORKDIR /djangoapi
# Upgrade pip
RUN pip install --upgrade pip
# Copy requirements.txt to the container
COPY ./requirements.txt .
# Install application dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
# Copy the application code to the container
COPY . .
# # Run database migrations
RUN python manage.py migrate --no-input
# Expose a port for the application
EXPOSE 8000
# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# docker build -t djangoapi .
# docker run -d -p 8002:8000 djangoapi 
