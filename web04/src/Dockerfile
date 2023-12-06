FROM python:3.11

WORKDIR /app

COPY ./src/ /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLAG="flag{d3f4ult_cr3d3nt14ls_are_always_a_bad_idea}"

EXPOSE 80

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
