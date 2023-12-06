FROM python:3.11

WORKDIR /app
COPY ./src/ /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLAG="flag{robots_will_take_over_the_world}"

EXPOSE 80

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
