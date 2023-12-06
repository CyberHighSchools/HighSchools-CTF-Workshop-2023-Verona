FROM python:3.11

COPY ./src/ /app
COPY ./flag.txt /flag.txt

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
