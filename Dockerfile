FROM python:3-slim-buster

EXPOSE 5000

COPY snowflake_data_profiler snowflake_data_profiler

RUN cd snowflake_data_profiler && python -m pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "-m", "snowflake_data_profiler.app"]
