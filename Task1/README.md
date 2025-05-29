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


2. **Configure Docker Hub Username for `deploy.sh`**:

    The `deploy.sh` script needs your Docker Hub username to tag and push the container image. It can be configured in one of two ways:
    *   **Environment Variable (Recommended):** Set the `DOCKERHUB_USERNAME` environment variable before running the script:
        ```bash
        export DOCKERHUB_USERNAME="your_dockerhub_username"
        ```
    *   **Interactive Prompt:** If the `DOCKERHUB_USERNAME` environment variable is not set, the script will prompt you to enter your Docker Hub username when you run it.

    Note: Before running the script, ensure your Docker CLI is logged in:
    ```bash
    docker login
    ```

3. **Update Kubernetes Deployment Configuration**:

    You *must* edit the Kubernetes deployment file `Task1/kubernetes/deployment.yaml` before deploying.
    Locate the following line:
    ```yaml
    image: YOUR_DOCKERHUB_USERNAME/rate-limiter:latest
    ```
    Replace `YOUR_DOCKERHUB_USERNAME` with your actual Docker Hub username. For example, if your username is `hrishidarade`, the line should look like:
    ```yaml
    image: hrishidarade/rate-limiter:latest
    ```
    This change is crucial for Kubernetes to pull the correct Docker image from your repository.


4. **Make the script executable**:
    ```bash
    chmod +x deploy.sh
    ```

5. **Start minikube**:
   ```bash
   minikube start --driver=docker
   ```

6. **Run the deployment script**:
   ```bash
    ./deploy.sh
    ```
    This script will build the Docker image, push it to Docker Hub, and deploy it to Minikube.

7. **Check the deployment status**:
    After running the script, you can check the status of the deployment using:
    ```bash
    kubectl get pods
    ```
    This will show you the status of the pods. Ensure that the pod is in the `Running` state.

8. **Access the service**:
    After the deployment, you can access the service using the service url and the exposed port. Run:
    ```bash
    minikube service rate-limiter-service --url
    ```
    This will give you the URL to access the rate limiter service.
    Maintain this terminal open to keep the service running.
    Open a new terminal to test the service.

##  Testing the Service
You can test the /submit endpoint using curl or a web browser:
```bash
curl -X GET <service-url>/submit
```
Example:

```bash
curl -X GET http://127.0.0.1:32658/submit
```
Hit the endpoint more than 5 times from the same IP to see the rate limiting in action. After 5 requests, you should receive a response:
```json
{
    "error": "Rate limit exceeded. Try again later."
}
```

## Cleanup
To clean up the resources created by the deployment script, you can run:
```bash
kubectl delete deployment rate-limiter
kubectl delete service rate-limiter-service
minikube stop
```

