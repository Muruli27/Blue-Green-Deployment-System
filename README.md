# DevOps-Based Blue-Green Deployment System

## Overview

The DevOps-Based Blue-Green Deployment System is a proof-of-concept project that demonstrates a zero-downtime deployment strategy using Docker containers. The project maintains two identical environments (Blue and Green), allowing seamless application updates while ensuring continuous availability and quick rollback in case of failures.

A sample Student Portal application is used to demonstrate the deployment process.

---

## Objectives

- Implement Blue-Green Deployment using Docker.
- Minimize application downtime during updates.
- Demonstrate containerized deployment.
- Provide seamless switching between application versions.
- Enable quick rollback in case of deployment failures.
- Improve deployment reliability and availability.

---

## Technologies Used

- Python 3
- Flask
- Docker
- Docker Compose
- Git
- GitHub
- Nginx (Load Balancer)
- Jenkins (CI/CD Concept)
- Kubernetes (Future Scope)

---

## Project Structure

```
Blue-Green-Deployment-System/
│
├── blue/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── green/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── nginx.conf
└── README.md
```

---

## Project Workflow

1. Developer updates the application source code.
2. Docker builds separate Blue and Green application images.
3. Docker Compose creates isolated containers.
4. The Blue environment serves the live application.
5. The updated application is deployed to the Green environment.
6. After verification, traffic is switched to the Green environment.
7. If any issue occurs, traffic can be switched back to the Blue environment.

---

## Features

- Blue-Green Deployment
- Docker Containerization
- Multiple Application Versions
- Zero/Near-Zero Downtime
- Easy Rollback
- Version Isolation
- Simple Web Interface

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Blue-Green-Deployment-System.git
cd Blue-Green-Deployment-System
```

### Build Containers

```bash
docker compose build
```

### Start Containers

```bash
docker compose up
```

### Access Application

Blue Environment

```
http://localhost:5001
```

Green Environment

```
http://localhost:5002
```

If Nginx Load Balancer is configured:

```
http://localhost
```

---

## Expected Output

- Blue Version of the Student Portal
- Green Version with additional functionality
- Seamless deployment demonstration
- Zero-downtime deployment concept

---

## Future Enhancements

- Jenkins CI/CD Pipeline
- Kubernetes Deployment
- Prometheus Monitoring
- Grafana Dashboard
- Automated Rollback
- Cloud Deployment (AWS/Azure)

---

## Team Members

- Muruli N (U23E01IS014)
- Darshan BS (U23E01IS002)
- Karthik RK (U23E01IS007)
- Veeekshith M Shetty (U23E01IS032)

---

## Guide

**Ms. Ananya Patil G P**

Department of Information Science & Engineering

GM University, Davanagere

---

## License

This project was developed for academic purposes as part of the Project Based Learning (UE23IS3604) course at GM University.
