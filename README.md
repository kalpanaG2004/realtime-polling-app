# 📊 Real-Time Polling App

A simple **real-time polling application** built using **FastAPI** and
**WebSockets**, with a lightweight frontend in **HTML, CSS, and
JavaScript**.\
This project demonstrates how modern web apps communicate with backend
services and handle live data updates.

------------------------------------------------------------------------

## ✨ Features

-   📋 Live poll with multiple options
-   🗳️ Vote submission via REST API
-   🔄 Real-time results using WebSockets
-   ♻️ Poll reset functionality

------------------------------------------------------------------------

## 🧱 Tech Stack

**Frontend** - HTML - CSS - JavaScript (Fetch API + WebSocket)

**Backend** - FastAPI - WebSockets - Uvicorn

**Deployment** - Azure App Service (Backend) - GitHub Pages (Frontend)

------------------------------------------------------------------------

## 🚀 How to Use

### 1️⃣ Open the Live App

Simply visit the frontend URL and start voting.

-   Select an option
-   Votes update live for all connected users

No setup required.

------------------------------------------------------------------------

## 🔗 API Endpoints (Backend)

  Method   Endpoint    Description
  -------- ----------- ----------------------------------
  GET      `/poll`     Get poll question & options\
  POST     `/vote`     Submit a vote\
  POST     `/reset`    Reset poll counts\
  WS       `/ws`       Live updates via WebSocket

------------------------------------------------------------------------

## 🛠 Run Locally

### Backend

``` bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Backend will run at:

    http://localhost:8000

------------------------------------------------------------------------

### Frontend

-   Open `index.html` directly in a browser
-   OR use a simple live server

``` bash
npx serve .
```

------------------------------------------------------------------------

## 🎓 What This Project Teaches

-   Client--Server communication
-   REST APIs vs WebSockets
-   Real-time data flow
-   CORS and deployment challenges
-   Moving from local development to production

------------------------------------------------------------------------

## 👩‍💻 Author

**Kalpana Gupta**\
Built as part of a learning-focused demo on real-time web applications.
