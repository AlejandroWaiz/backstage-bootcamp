FROM python:3.10-alpine

COPY requeriments.txt /tmp

RUN pip install -r /tmp/requeriments.txt

COPY ./src /src

CMD ["python", "/src/app.py"]
