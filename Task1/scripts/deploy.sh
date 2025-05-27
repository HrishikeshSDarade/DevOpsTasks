#!/bin/bash

set -e

DOCKER_USERNAME="hrishidarade"
IMAGE_NAME="rate-limiter"
IMAGE_TAG="latest"

docker build -t $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG .

docker push $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG

kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
