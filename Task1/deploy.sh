#!/bin/bash

set -e

if [ -z "$DOCKERHUB_USERNAME" ]; then
    read -p "Enter your Docker Hub username: " DOCKERHUB_USERNAME
fi

DOCKER_USERNAME="$DOCKERHUB_USERNAME"

if [ -z "$DOCKER_USERNAME" ]; then
    echo "Docker Hub username is required. Exiting."
    exit 1
fi

IMAGE_NAME="rate-limiter"
IMAGE_TAG="latest"

docker build -t $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG .

docker push $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG

kubectl apply -f kubernetes/redis-deployment.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
