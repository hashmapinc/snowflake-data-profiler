FROM python:3

ENV FLASK_APP profiler-app.py

EXPOSE 5000

COPY app .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["flask","run"]
