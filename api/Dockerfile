FROM python:3.12 as dev

WORKDIR /usr/src/app

# install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["manage.py", "--debug", "run", "--host", "0.0.0.0"]

FROM python:3.12 as prod

WORKDIR /usr/src/app

# install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY .. .

ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:5000", "server:app"]
