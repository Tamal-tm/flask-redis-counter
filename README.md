# Flask + Redis Visit Counter — Dockerized, K8s-ready, CI/CD-automated

A small Flask app backed by Redis, containerized with Docker, deployable to
Kubernetes, with an automated GitHub Actions pipeline that builds and pushes
the image to Docker Hub on every push to `main`.

```
flask-redis-counter/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── docker-compose.yml
├── k8s/
│   ├── web-deployment.yaml
│   ├── web-service.yaml
│   ├── redis-deployment.yaml
│   └── redis-service.yaml
├── .github/
│   └── workflows/
│       └── docker-build.yml
└── README.md
```

## Architecture

```
┌─────────────┐      ┌──────────────┐
│   Browser   │─────▶│  Flask (web) │
└─────────────┘      │  2 replicas  │
                      └──────┬───────┘
                             │
                      ┌──────▼───────┐
                      │    Redis     │
                      │  1 replica   │
                      └──────────────┘
```

- **Local dev**: Docker Compose runs both services on one machine.
- **Deployment**: Kubernetes Deployments + Services (tested on minikube).
- **CI/CD**: GitHub Actions builds the image and pushes to Docker Hub on
  every push to `main`.

## Run locally (Docker Compose)

```bash
docker compose up --build
```
Visit `http://localhost:5000`.

## Deploy to Kubernetes (minikube)

```bash
minikube start --driver=docker
kubectl apply -f k8s/
minikube service web-service --url
```

## CI/CD

Pushing to `main` triggers `.github/workflows/docker-build.yml`, which builds
the Docker image and pushes it to Docker Hub as `:latest` and `:<commit-sha>`.

## Tech stack
Flask, Redis, Docker, Docker Compose, Kubernetes, GitHub Actions
