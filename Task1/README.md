# Rate Limiter Service

A lightweight Python-based rate-limiting API that blocks IPs after exceeding a request threshold. This service is containerized with Docker and deployed to Kubernetes via a deployment script.

## Prerequisites

Ensure these are installed:

- [Docker](https://www.docker.com/get-started)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)
- Bash (Linux/macOS or Git Bash for Windows)


## Getting Started   
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HrishikeshSDarade/DevOpsTasks.git
   cd Task1
   ```

2. **Navigate to the script directory**:
    ```bash
    cd script
    ```
    IN the script directory, you will find the `deploy.sh` file which contains the deployment script.
    🔐 Note: Before running the script, ensure your Docker CLI is logged in using:
    ```bash
    docker login
    ```
    You need to replace the `DOCKERHUB_USERNAME` with your Docker Hub credentials in the script.

3. **Make the script executable**:
    ```bash
    chmod +x deploy.sh
    ```

4. **Start minikube**:
   ```bash
   minikube start --driver=docker
   ```

5. **Run the deployment script**:
   ```bash
    ./deploy.sh
    ```
    This script will build the Docker image, push it to Docker Hub, and deploy it to Minikube.

6. **Check the deployment status**:
    After running the script, you can check the status of the deployment using:
    ```bash
    kubectl get pods
    ```
    This will show you the status of the pods. Ensure that the pod is in the `Running` state.

7. **Access the service**:
    After the deployment, you can access the service using the service url and the exposed port. Run:
    ```bash
    minikube service rate-limiter-service --url
    ```
    This will give you the URL to access the rate limiter service.
    Maintain this terminal open to keep the service running.
    Open a new terminal to test the service.

## 🧪 Testing the Service
You can test the /submit endpoint using curl or a web browser:
```bash
curl -X GET <service-url>/submit
curl -X POST <service-url>/submit
```
Example:

```bash
curl -X GET http://127.0.0.1:32658/submit
```


## Cleanup
To clean up the resources created by the deployment script, you can run:
```bash
kubectl delete deployment rate-limiter
kubectl delete service rate-limiter-service
minikube stop
```

