Project: Automated CI/CD Pipeline for Containerized Web Applications
1. The Tech Stack
OS Environment: Windows 11 + WSL2 (Ubuntu Linux)

Containerization: Docker & Docker Hub

Orchestration: Kubernetes (K8s) via Docker Desktop

CI/CD Automation: GitHub Actions

Application: Python (Flask) Web Server

Version Control: Git

2. Implementation Phases (The "How-To")
Phase 1: Environment Setup
WSL2 Integration: Configured Windows Subsystem for Linux (WSL2) to allow running native Linux commands on Windows.

Docker Configuration: Enabled "Use WSL 2 based engine" in Docker Desktop and linked it to the Ubuntu distro.

Key Challenge Solved: Fixed authentication errors by verifying the Docker Hub email and regenerating Access Tokens.

Phase 2: Containerization (Docker)
We moved the application from "running locally" to "running anywhere."

Dockerfile: Created a recipe to package Python, the dependencies (flask), and the source code.

Base Image: python:3.9-slim (Lightweight OS).

Port Mapping: Mapped container port 5000 to host port 5000 using -p 5000:5000.

Registry: Pushed the custom image to Docker Hub so it can be accessed globally.

Phase 3: Orchestration (Kubernetes)
We moved from running one container to running a "Self-Healing Fleet."

Deployment (deployment.yaml):

High Availability: Configured replicas: 3 to ensure 3 copies are always running.

Rolling Updates: Set imagePullPolicy: Always to force K8s to download the newest code version during updates.

Service (service.yaml):

Load Balancing: Created a LoadBalancer service to act as a "front door," distributing traffic across the 3 pods and exposing the app to localhost:5000.

Phase 4: Automation (CI/CD)
We removed the need to manually build and push code.

GitHub Actions (deploy.yml): Created a workflow that triggers on every git push.

On Why You Used Docker:

"I used Docker to solve the 'it works on my machine' problem. By packaging the Python environment and dependencies into a container, I ensured consistency across development and production."

On Why You Used Kubernetes:

"Running a single container is risky. I used Kubernetes to orchestrate a fleet of replicas. This gave the application High Availability—if one pod crashes, K8s automatically spins up a replacement (Self-Healing)."

On Why You Used CI/CD:

"I wanted to eliminate manual deployment errors. I set up a GitHub Actions pipeline that automatically builds and pushes the Docker image whenever code is committed. This allows for rapid iteration and ensures that the Docker Hub registry always has the latest version."

CI Steps: Checks out code -> Logs into Docker Hub -> Builds Image.

CD Steps: Pushes the new image to Docker Hub with the latest tag.

Security: Used GitHub Secrets (DOCKER_USERNAME, DOCKER_PASSWORD) to hide credentials.

Key Challenge Solved: Resolved a Git "Permission Denied" error by generating a Personal Access Token (PAT) with both repo and workflow scopes.
