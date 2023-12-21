# nutriscan-backend-flask
Endpoint for predictions

# Installation
1. Authenticate docker
```shell
docker login
```
2. Clone the repo
```shell
git clone https://github.com/AdityaP1502/nutriscan-backend-flask
cd nutriscan-backend-flask
```

3. Get the model
```shell
mkdir tf-model
wget https://storage.googleapis.com/nutriscan-capstone/model.h5 -p tf-model/
``` 

4. Build the container
```shell
docker build -t ml-endpoint:latest .
```

5. Run the container
```shell
docker run -p [HOST PORT]:3000 -d ml-endpoint:latest
```
