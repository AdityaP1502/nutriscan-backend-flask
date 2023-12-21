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
wget https://storage.googleapis.com/nutriscan-capstone/model.h5 -P tf-model/
``` 

# Deploy (Local)
1. Build the container
```shell
docker build -t ml-endpoint:latest .
```

2. Run the container
```shell
docker run -p [HOST PORT]:3000 -d ml-endpoint:latest
```

# Deploy (Cloud Run)
```shell
docker build -t nutriscan-ml-app:v1.0 .
docker tag nutriscan-ml-app:v1.0    asia-southeast2-docker.pkg.dev/nutriscan-capstone/nutriscan-image-repo/nutriscan-ml-app:v1.0
docker push asia-southeast2-docker.pkg.dev/nutriscan-capstone/nutriscan-image-repo/nutriscan-ml-app:v1.0
gcloud run deploy nutriscan-api   --image=asia-southeast2-docker.pkg.dev/nutriscan-capstone/nutriscan-image-repo/nutriscan-ml-app:v1.0 --allow-unauthenticated --region asia-southeast2
```

