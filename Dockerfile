FROM python:3.11 as python-base
RUN mkdir api
WORKDIR  /api
COPY /pyproject.toml /poetry.lock
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:8000", "backend.__main__:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]
