# Use the Python3.7.2 image
FROM python:3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
# ADD . /app
ADD requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run the command to start uWSGI with autoreload
CMD ["uwsgi", "app.ini", "--py-autoreload", "1"]
