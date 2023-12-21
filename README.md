# nutriscan-backend-flask
Endpoint for predictions

# Installation
1. Authenticate docker
```shell
docker login
```
2. Get the model
```
mkdir tf-model; wget https://storage.googleapis.com/nutriscan-capstone/model.h5 -p tf-model/
``` 

3. Build the container
```shell
docker build -t ml-endpoint:latest .
```

4. Run the container
```shell
docker run -p [HOST PORT]:3000 -d ml-endpoint:latest
```
