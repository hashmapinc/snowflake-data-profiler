devserver:
	python -m python -m snowflake_data_profiler.app

venv:
	python3 -m venv venv && source ./venv/bin/activate && pip install --upgrade pip

activate_venv:
	source ./venv/bin/activate

image:
	docker build -t snowflake_data_profiler .

container:
	docker run -it -p 5000:5000 snowflake_data_profiler
