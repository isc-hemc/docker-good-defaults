FROM python:3.7

COPY app /app

WORKDIR /app

RUN pip install pipenv
RUN pipenv install

CMD [ "pipenv", "run", "uwsgi", "run.ini" ]