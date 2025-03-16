FROM custom-image:v1
RUN mkdir /fastapiapp
WORKDIR /fastapiapp
COPY . /fastapiapp
RUN poetry add /util_package
RUN poetry install
CMD [ "poetry", "run", "fastapi", "dev", "fastapiapp", "--host", "0.0.0.0", "--port", "8001" ]