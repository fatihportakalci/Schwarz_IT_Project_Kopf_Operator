FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY kopf_operator.py kopf_operator.py

CMD ["python", "kopf_operator.py"]
