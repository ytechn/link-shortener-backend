FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]