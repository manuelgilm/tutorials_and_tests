FROM python:3.11 
RUN mkdir /multicontainer
WORKDIR /multicontainer
COPY . /multicontainer/
RUN pip install poetry 
RUN poetry install
CMD ["poetry", "run", "fastapi", "dev", "multicontainer", "--port", "8000", "--host", "0.0.0.0"]