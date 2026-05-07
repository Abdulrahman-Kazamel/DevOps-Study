
```bash
docker login

docker build -t your-username/my-app:v1.0 .
#or if image already exist
docker tag local-image-name your-username/my-app:v1.0
docker tag flask-app:1.0 abdulrahmankazamel/flask-app
docker push your-username/my-app
```