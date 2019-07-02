install-deps:
	pip install -r ./deps/requirements.in

test:
	PYTHONPATH=./src/ pytest ./tests/ -vv

sync-deps:
	pip-compile -o ./deps/requirements.txt ./deps/requirements.in
