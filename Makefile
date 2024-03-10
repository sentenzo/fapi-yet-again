CODE = app



run:
	poetry run uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload


export_requirements:
	poetry export --without-hashes --with dev -f requirements.txt --output requirements.txt

lint:
	poetry run isort ${CODE}
	poetry run black ${CODE}
	poetry run flake8 ${CODE} --count --show-source --statistics
	poetry run mypy ${CODE}