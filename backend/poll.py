# poll state & model
from pydantic import BaseModel

poll_question = "Which domain excites you the most?"

poll_options = {
    "Web Development": 0,
    "AI/ML": 0,
    "Cloud Computing": 0
}

active_connections = []

class VoteRequest(BaseModel):
    option: str