# 🚀 Scalable ML Model Deployment with Docker & Kubernetes

## 📌 Overview

This project demonstrates how to take a Machine Learning model from development to a **production-like scalable system** using modern tools.

Instead of just building a model, this project focuses on:

* Serving the model via an API
* Containerizing the application
* Deploying it on Kubernetes
* Enabling scalability

---

## 🧠 Problem Statement

Most ML projects stop at training a model.
This project solves the real-world problem of:

> “How do we deploy and scale a machine learning model in production?”

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Docker
* Kubernetes (Minikube)
* Uvicorn

---

## 🏗️ Architecture

User → API Request → Kubernetes Service → Pod → ML Model → Response

---

## 🔄 Workflow

1. Train a Machine Learning model (`train.py`)
2. Save the trained model (`model.pkl`)
3. Build an API using FastAPI (`app.py`)
4. Containerize using Docker (`Dockerfile`)
5. Deploy on Kubernetes (`deployment.yaml`)
6. Expose service (`service.yaml`)
7. Enable auto-scaling (HPA)

---

## 📦 Project Structure

```
ml-platform/
│── app.py
│── train.py
│── model.pkl
│── requirements.txt
│── Dockerfile
│── deployment.yaml
│── service.yaml
│── .gitignore
```

---

## 🚀 How to Run Locally

### 1. Clone the repo

```
git clone https://github.com/your-username/ml-platform.git
cd ml-platform
```

### 2. Run with Docker

```
docker build -t ml-model-api .
docker run -p 8000:8000 ml-model-api
```

### 3. Access API

```
http://localhost:8000/docs
```

---

## ☸️ Run with Kubernetes (Minikube)

### Start cluster

```
minikube start --driver=docker
```

### Load image

```
minikube image load ml-model-api
```

### Deploy

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Access service

```
minikube service ml-model-service
```

---

## 📈 Auto Scaling

Enable HPA:

```
kubectl autoscale deployment ml-model-deployment \
  --cpu-percent=50 \
  --min=1 \
  --max=5
```

---

## 🧪 API Example

### Endpoint:

```
POST /predict
```

### Request:

```json
{
  "number": 4
}
```

### Response:

```json
{
  "prediction": 1
}
```

---

## 🎯 Key Features

* ✅ End-to-end ML deployment
* ✅ REST API for predictions
* ✅ Docker containerization
* ✅ Kubernetes deployment
* ✅ Horizontal scaling
* ✅ Production-like architecture

---

## 📚 What I Learned

* Difference between model development and deployment
* Containerization using Docker
* Kubernetes concepts (Pods, Services, Deployments)
* Scaling applications using HPA
* Building real-world ML systems

---

## 🚀 Future Improvements

* Add real-world dataset
* Deploy on cloud (AWS/GCP)
* Add monitoring (Prometheus + Grafana)
* Implement model versioning
* Add authentication & security

---

## 👨‍💻 Author

**Hrishi Menon M**

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!
