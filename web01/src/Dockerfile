FROM python:3.11

WORKDIR /app

COPY ./src/ /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLAG="flag{here_is_your_c00ki3_:3}"

EXPOSE 80

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
