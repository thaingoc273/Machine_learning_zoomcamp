FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy
COPY ["predict.py", "model.bin", "predict_test.py", "./"]

EXPOSE 9696
# ENTRYPOINT [ "gunicorn", "--bind=localhost:9696", "predict:app" ]
ENTRYPOINT [ "waitress-serve", "--listen=localhost:9696", "predict:app"]