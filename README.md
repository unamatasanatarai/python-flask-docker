# DOCKER FLASK PYTHON 3:latest

`docker-compose up -d`

for NOT RELOADING change: `CMD ["uwsgi", "app.ini", "--py-autoreload", "1"]` into `CMD ["uwsgi", "app.ini"]`
  in `/flask/Dockerfile`

```
export FLASK_APP=run.py
flask run
```