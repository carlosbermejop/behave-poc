  FROM python:3.14.3-slim-trixie

  WORKDIR /usr/src/server
  COPY ./server/requirements.txt requirements.txt

  RUN pip install -r requirements.txt

  CMD ["flask", "--app", "server", "run", "--host=0.0.0.0"]