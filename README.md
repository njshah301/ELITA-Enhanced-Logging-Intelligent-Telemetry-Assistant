
# 🚀 Project Name


## 📌 Table of Contents
- [Introduction](#introduction)

- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)

---

## 🎯 Introduction
This project automates ServiceNow incident resolution using an AI-driven approach. The system consists of two key backend components:

1. **Optimus Agent**: Pulls unassigned incidents from ServiceNow, determines the assignment group, and assigns the incident to the respective platform owner.
2. **Vertical Agent**: An AI-powered agent with a knowledge base that assists in resolving incidents efficiently.

## 🔧 Tech Stack
- **Backend**: Python, Django
- **Database**: MongoDB
- **Containerization**: Docker
- **API Testing**: Postman
- **Cloud & Deployment**: Azure
- **AI & NLP**: OpenAI (text-embedding-3-small), gpt-3o
- **ITSM Integration**: ServiceNow


  
 
🖼️ Screenshots:

![Screenshot 1](link-to-image)


## 🚀 Features
✅ **Automated Incident Assignmen and management** using ServiceNow API  
✅ **AI-powered Resolution Engine** with automation capabilities  
✅ **Chatbot Assistance** for logs, metrics, and recommendations  
✅ **Seamless Deployment with Docker & Azure**  

## 💡 Inspiration
We have large number of support engineers across the organization who provide application and infrastructure support across L1/L2/L3 levels. This requires troubleshooting, accessing variety of knowledge base articles, running automations, reviewing telemetry data and metrics, health metrics, etc. This process requires lot of context switching leading to significant time and effort overhead for the support engineer.


## ⚙️ What It Does
Team-specific AI agent will help the support engineer resolve an incident using AI capabilities. 

## 🛠️ How We Built It
This consists of one agent which fetches data from Servicenow tool and send it to the respective vertical agents which will help support enginner to solve the issue of that incident in quicker manner.

### 🔹 Incident Assignment Flow
1. **Data Retrieval**:
   - The **Optimus Agent** fetches all unassigned incidents from ServiceNow.
   - It checks the **assignment group** and assigns the incident to the **platform owner**.

2. **AI-Driven Assistance**:
   - The **Vertical Agent** receives the incident and checks for possible automation.
   - If automation is available, the incident is auto-resolved.
   - If no automation exists, the agent searches the **knowledge base** (logs, dashboards, past incidents, and knowledge articles).

3. **Support Engineer Interaction**:
   - If further action is required, a support engineer can interact with the AI chatbot.
   - The chatbot provides recommendations, retrieves logs for specific time ranges, and allows document uploads for better context.
   - The support engineer can also fetch **logs, metrics, and tracing information** directly within the chat.

4. **Incident Resolution**:
   - The engineer finds the resolution and **closes the incident from the UI itself**.
   
## ⚙️ Workflows 
### [1] Application Overview

![image](https://github.com/user-attachments/assets/a4dbb98d-fe8e-4ba9-a95a-dc8b26f47ce3)

### [2] Agent Overview 

![image](https://github.com/user-attachments/assets/629a744a-9274-49dd-b02d-02e92663b6b7)



## 🚧 Challenges We Faced

1. **Tight Deadlines**: Since this project was built for a hackathon, we had a very limited time to develop both the backend and frontend, containerize the application, and deploy it on Azure.
2. **Scalability of AI Agent**: Ensuring that the AI agent could handle increasing workloads was a challenge. We addressed this by implementing a **microservices-based architecture** that supports horizontal scalability.
3. **Deployment Complexity**: Deploying the system on an **Azure VM** with multiple containers required careful orchestration and configuration.
4. **Implementing RAG (Retrieval-Augmented Generation)**: Ensuring that the AI agent retrieved the most **accurate and relevant** data for incident resolution was a key challenge that required fine-tuning our retrieval mechanisms and knowledge base.
5. **ServiceNow Integration**: Efficiently fetching incidents and managing updates in real-time while ensuring API rate limits and consistency posed integration challenges.


## 🏃 How to Run
# 🚀 How to Run the Optimus App & Agent Containers

## 📌 Prerequisites
Ensure you have **Docker** installed on your system. If not, install it using:

```sh
sudo apt update && sudo apt install docker.io -y
```

## 🔹 Step 1: Pull Docker Images
Download the latest images from Docker Hub:

```sh
sudo docker pull njshah301/optimus-app:1.0.0
sudo docker pull njshah301/agent:1.0.0
```

## 🔹 Step 2: Create a Docker Network
Create a custom Docker network named **quantam**:

```sh
sudo docker network create quantam
```

## 🔹 Step 3: Run the Agent Container
Start the **Agent** container and connect it to the `quantam` network:

```sh
sudo docker run --env-file .env -d --network=quantam --name agent -p 80:80 njshah301/agent:1.0.0
```

## 🔹 Step 4: Run the Optimus Container
Start the **Optimus** container and connect it to the `quantam` network:

```sh
sudo docker run --env-file .env -d --network=quantam --name optimus njshah301/optimus:1.0.0
```

## ✅ Step 5: Verify Running Containers
Check if both containers are running:

```sh
sudo docker ps
```
```sh
sudo docker ps
```

## ✅ Step 6: Service Now login
```[Check if both containers are running:](https://dev305595.service-now.com/now/nav/ui/classic/params/target/incident_list.do%3Fcaller_id%3Djavascript%253Ags.getUserID%2528%2529%255Eactive%253Dtrue%255Euniversal_requestISEMPTY%26sysparm_query%3Dcaller_id%253Djavascript%253Ags.getUserID%2528%2529%255Eactive%253Dtrue%255Euniversal_requestISEMPTY%255EEQ%26sysparm_view%3Dess)```
```
Username: admin
Password: pu!ycN3Q7/XX

```

