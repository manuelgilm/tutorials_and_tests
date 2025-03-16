# Creating custom image with Python package

This tutorial provides instructions on how to create a custom Docker image that includes a Python package. 

## creating the base image

run 
`docker build -t <base-image>:<tag> .`

## To use the custom image just use it in your docker file as.

`FROM <base-image>:<tag>` 

### Example:

run: 
```bash
cd fastapiapp
docker build -t fastapiapp:v1 .
docker run -it -p 8001:8001 fastapiapp:v1
```


