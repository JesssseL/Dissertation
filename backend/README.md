# Backend Application

## Overview
This is the backend of the AI-Assisted Shopping System being developed as part of a dissertation project. The backend is implemented using FastAPI.

## Technologies
- FastAPI
- Pydantic
- Uvicorn

## Project Structure
```
app/
├── clients/		   Connections to external API clients
├── models/			   Request and response models
├── services/          API logic and external services
├── config.py          Configuration and environment settings
└── main.js            Application entry point
```

# Environment
The backend application was developed and tested with the following environment:
- python v3.14.4
- pip v26.1.1
- fastapi v0.136.1

## Installation
```
pip install -r requirements.txt
```

## Run Development Server
```
.venv\Scripts\Activate.ps1
fastapi dev
```

Interactive documentation application will normally run at:
http://localhost:8000/docs

## Run Production Version
```
.venv\Scripts\Activate.ps1
fastapi run
```
