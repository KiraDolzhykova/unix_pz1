FROM python:3.12

RUN pip install Flask

COPY . /app
WORKDIR /app

ENV FLASK_RUN_PORT 4000

CMD ["flask", "run", "--host=0.0.0.0"]
