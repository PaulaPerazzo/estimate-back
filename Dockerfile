FROM python:3.10.7

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

WORKDIR /app/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0",  "--reload",  "--port", "8000"]