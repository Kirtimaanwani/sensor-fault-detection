
# Sensor-Fault-Detection

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. Git Actions

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage.

## Data Collections
![image](./flowcharts/data%20pipeline.drawio.png)

## Project Architecture
![image](./flowcharts/Project%20architecture.drawio.png)


## Deployment Architecture
![image](./flowcharts/deployment%20architecture.drawio.png)


### Step 1: Clone the repository
```bash
git clone https://github.com/Kirtimaanwani/sensor-fault-detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -p venv/ python=3.8 -y
```

```bash
conda activate venv/
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export MONGODB_URL="Paste your mongoDB Url here"

sample_url = mongodb+srv://<user_name>:<password>@cluster0.1p6mzvm.mongodb.net/test

```

### Step 5 - Run the application server
```bash
python main.py
```

### Step 6. Train application
```bash
http://localhost:8080/train

```

### Step 7. Prediction application
```bash
http://localhost:8080/predict

```

## Run locally

1. Check if the Dockerfile is available in the project directory


2. Build the Docker image
```
docker build --build-arg MONGODB_URL=<MONGODB_URL>
```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```


