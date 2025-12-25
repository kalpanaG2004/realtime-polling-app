from fastapi import WebSocket, WebSocketDisconnect
from .poll import poll_question, poll_options, active_connections, VoteRequest

def register_routes(app):

    @app.get("/poll")
    def get_poll():
        return {
            "question": poll_question,
            "options": poll_options
        }

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

    @app.post("/reset")
    def reset_poll():
        for key in poll_options:
            poll_options[key] = 0
        return {
            "message": "Poll Reset",
        }