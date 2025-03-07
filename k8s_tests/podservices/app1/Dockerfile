FROM python:3.11
RUN mkdir /app1
COPY . /app1
WORKDIR /app1
RUN pip install poetry 
RUN poetry install
CMD ["poetry", "run", "fastapi", "dev", "app1", "--host","0.0.0.0", "--port", "8000"]