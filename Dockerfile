FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --root-user-action=ignore requests

ENV TZ=Asia/Shanghai

ENV CONTAINER_SCRIPT=/app

CMD sh -c "cd $CONTAINER_SCRIPT && ls && pip install -r requirements.txt && python run.py -c true && python run.py"
