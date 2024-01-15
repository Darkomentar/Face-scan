# import asyncio
# import websockets
# import json

# async def connect_to_websocket():
#     uri = "ws://localhost:8000/history/ws" 
#     async with websockets.connect(uri) as websocket:
        
#         data_to_send = json.dumps({
#             "id_p": 7,
#             "photo": "url"
#         })
#         await websocket.send(data_to_send)

       
#         response = await websocket.recv()
#         print(f"Ответ от сервера: {response}")


# asyncio.run(connect_to_websocket())

import asyncio
import websockets
import json
import base64

async def connect_to_websocket():
    uri = "ws://localhost:8000/history/ws" 
    async with websockets.connect(uri) as websocket:

        image_path = './ilnaz.jpg'
       
        with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        data_to_send = json.dumps({
            "id_p": 7,
            "photo": encoded_image
            })
        await websocket.send(data_to_send)
        response = await websocket.recv()

      

asyncio.run(connect_to_websocket())
