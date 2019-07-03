install-deps:
	pip install -r ./deps/requirements.in

test:
	PYTHONPATH=./src/ pytest ./tests/ -vv

sync-deps:
	pip-compile -o ./deps/requirements.txt ./deps/requirements.in

clean:
	rm -rf `find . -type d -name ".pytest_cache"`
	rm -rf `find . -type d -name "*.eggs"`
	rm -rf `find . -type d -name "*.egg-info"`
	rm -rf `find . -type d -name "__pycache__"`
	rm -rf `find . -type f -name "*.pyc"`
	rm -rf `find . -type f -name "*.pyo"`

	rm -f junit_results.xml .coverage
	rm -rf build dist coverage .mypy_cache .eggs
