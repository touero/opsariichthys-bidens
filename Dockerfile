FROM python:3.8.8-slim-buster

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src

CMD ["python", "local_runner.py"]