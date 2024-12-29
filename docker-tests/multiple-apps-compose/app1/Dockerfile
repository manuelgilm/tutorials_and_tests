FROM python:3.9 
RUN mkdir /app1
WORKDIR /app1
COPY . /app1
ENV PYTHONPATH ${PYTHONPATH}:${PWD}
RUN pip3 install poetry 
RUN poetry install 

CMD ["poetry", "run", "fastapi","dev", "app1", "--host","0.0.0.0", "--port", "8000"]
