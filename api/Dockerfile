# Use the official Python image from the Docker Hub as the base image for the development stage
FROM python:3.12 as dev

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./
# Install the dependencies specified in the requirements file
RUN pip install -r requirements.txt

# Set the entry point and default command for the development stage
ENTRYPOINT ["python"]
CMD ["manage.py", "--debug", "run", "--host", "0.0.0.0"]

# Use the official Python image from the Docker Hub as the base image for the production stage
FROM python:3.12-alpine as prod

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./
# Install the dependencies specified in the requirements file
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the entry point and default command for the production stage
ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:5000", "server:app"]
