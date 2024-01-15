from fastapi import FastAPI
from app.history.router import router as router_history_ws
from app.people.router import router as router_peoples
from app.detect_history.router import router as router_detect_history

app = FastAPI()

app.include_router(router_history_ws)
app.include_router(router_peoples)
app.include_router(router_detect_history)