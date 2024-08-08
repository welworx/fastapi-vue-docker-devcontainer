FROM python:3.12

COPY pyproject.toml /code/
COPY ./app /code/

WORKDIR /code/app

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry install

EXPOSE 8000
CMD ["poetry", "run", "python", "-m", "uvicorn", "--reload", "--host=0.0.0.0", "--port=8000", "main:app"]