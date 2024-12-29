FROM python:3.9 
RUN mkdir /app2
WORKDIR /app2
COPY . /app2
ENV PYTHONPATH ${PYTHONPATH}:${PWD}
RUN pip3 install poetry 
RUN poetry install 

CMD ["poetry", "run", "fastapi","dev", "app2", "--host","0.0.0.0", "--port", "8001"]
