FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy
COPY ["predict.py", "model.bin", "predict_test.py", "./"]

EXPOSE 2727
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:2727", "predict:app" ]
# ENTRYPOINT [ "waitress-serve", "--listen=localhost:2727", "predict:app"]