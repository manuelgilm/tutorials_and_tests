FROM python:3.9 
RUN mkdir backend
WORKDIR /backend
COPY . /backend/
ENV PYTHONPATH="${PYTHONPATH}:${PWD}"
RUN pip3 install poetry
RUN poetry install 

CMD ["poetry", "run", "fastapi", "dev", "backend", "--host","0.0.0.0","--port","8000"]