#!/bin/bash
set -e

# List services
echo " Listing available services..."
kubectl get services

SERVICE_URL=$(minikube service rate-limiter-service --url 2>/dev/null | tail -n1)

echo " Retrieved URL: $SERVICE_URL"

if [[ -z "$SERVICE_URL" ]]; then
  echo "Failed to retrieve the Minikube service URL."
  exit 1
fi

echo " Using service URL: $SERVICE_URL"

for i in {1..10}; do
  echo -e "\n Request $i:"
  curl -s -H "X-Forwarded-For: 192.168.1.100" "$SERVICE_URL/submit"
done