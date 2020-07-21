devserver: venv
	source ./venv/bin/activate && python -m snowflake_data_profiler.app

venv:
	python3 -m venv venv && source ./venv/bin/activate && \
	  pip install --upgrade pip && \
	  pip install -r snowflake_data_profiler/requirements.txt

image:
	docker build -t snowflake_data_profiler .

container:
	docker run -it -p 5000:5000 snowflake_data_profiler
