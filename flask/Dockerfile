FROM python:3-stretch

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
	&& pip install -r requirements.txt

# run the command to start uWSGI with autoreload
CMD ["uwsgi", "app.ini", "--py-autoreload", "1"]
