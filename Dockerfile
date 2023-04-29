FROM python:3.8.8-slim-buster
COPY allSchoolAPI /allSchoolAPI

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /allSchoolAPI

CMD ["python", "./src/local_runner.py"]