FROM python:3.9.13-slim

COPY . /app
WORKDIR /app

RUN python3 -m venv venv /opt/venv

RUN   /opt/venv/bin/pip install pip --upgrade  &&\
      /opt/venv/bin/pip install -r requirements.txt &&\
      chmod +x entrypoint.sh &&\
      /opt/venv/bin/python manage.py collectstatic --noinput

CMD ["/app/entrypoint.sh"]