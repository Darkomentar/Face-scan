from datetime import datetime
from fastapi import APIRouter, FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import json

from app.detect_history.router import find_last_n_with_names
from app.people.router import get_people
from app.detect_history.dao import Detect_historyDAO

router = APIRouter(
    prefix='/history',
    tags=["History"]
)

# Инкрементация номера
global number 
number = -1
async def increment_number():
    global number 
    if number == -1:
        number = await find_last_n_with_names(1)
        number = number[0]["id"]
    else:
        number += 1
    return number


async def serch_number(id):
    name_response = await get_people(id)
    name_data = name_response
    return name_data.fio

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, websocket: WebSocket):
        try:
            response_data = {
                "ERR": 0
            }
            await websocket.send_text(json.dumps(response_data))
            print(f"Ошибка при отправке сообщения: 0")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")


    # async def broadcast(self, message: str):
    #     for connection in self.active_connections:
    #         await connection.send_text(message)
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")

manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data_dict = await websocket.receive_json()
            name = ""
            photo = ""
            try:
                id_p = data_dict.get("id_p", "Unknown")
                name = await serch_number(id_p)
                photo = data_dict.get("photo", "Unknown")
                await Detect_historyDAO.add_new_detect_history(id_p, datetime.now(), photo)
            except Exception as e:
                print(f"Ошибка при обработке данных: {e}")
               

            response_data = {
                "id": await increment_number(),
                "name_people": name,
                "date_time": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                "photo": photo
            }

            await manager.broadcast(json.dumps(response_data))
            await manager.send_personal_message(websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
     
