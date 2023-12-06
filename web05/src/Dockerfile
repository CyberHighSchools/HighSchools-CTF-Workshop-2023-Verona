FROM python:3.11

WORKDIR /app
COPY ./src/ /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLAG="flag{was_the_qu3sti0n_t00_easy?}"

EXPOSE 80

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
