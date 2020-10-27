FROM python:3.7-slim-buster

EXPOSE 5000

COPY snowflake_data_profiler snowflake_data_profiler

RUN cd snowflake_data_profiler && pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "3600", "--workers=5", "snowflake_data_profiler.wsgi:app"]
