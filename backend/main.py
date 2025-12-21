from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import WebSocket, WebSocketDisconnect

app = FastAPI(title="Real-Time Polling App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

poll_question = "Which domain excites you the most?"

poll_options = {
    "Web Development": 0,
    "AI/ML": 0,
    "Cloud Computing": 0
}

active_connections = []

@app.get("/poll")
def get_poll():
    return {
        "question": poll_question,
        "options": poll_options
    }

class VoteRequest(BaseModel):
    option: str

@app.post("/vote")
async def submit_vote(vote: VoteRequest):
    if vote.option not in poll_options:
        return {"error": "Invalid Option"}
    poll_options[vote.option] += 1

    # Broadcast updated results to all connected clients
    for connection in active_connections:
        await connection.send_json(poll_options)

    return {
        "message": "Vote recorded",
        "results": poll_options
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    # Send Current results immediately on connect
    await websocket.send_json(poll_options)

    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections.remove(websocket)
