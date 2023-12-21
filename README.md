# nutriscan-backend-flask
Endpoint for predictions

# Installation
1. Authenticate docker
```shell
docker login
```

2. Build the container
```shell
docker build -t ml-endpoint:latest .
```

3. Run the container
```shell
docker run -p [HOST PORT]:3000 -d ml-endpoint:latest
```
