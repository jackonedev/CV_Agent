install:
	python -m pip install --upgrade pip
	cd ./knowledge-graph-ingest && pip install -r requirements.txt
	cd ..
	cd ./langgraph-agent && pip install -r requirements.txt


format:
	isort --profile=black --skip .venv . &&\
	autopep8 --in-place ./*/*.py &&\
	black --line-length 79 . --exclude '(\.venv)'

lint-ingest:
	cd ./knowledge-graph-ingest && pylint --disable=R,C ./*.py

lint-agent:
	cd ./langgraph-agent && pylint --disable=R,C ./*.py