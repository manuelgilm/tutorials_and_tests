FROM python:3.12-slim
RUN mkdir /simpleapp
WORKDIR /simpleapp
COPY . /simpleapp/

RUN pip install poetry 
RUN poetry install

CMD ["poetry", "run", "fastapi", "dev", "simpleapp", "--host","0.0.0.0", "--port", "8000"]
