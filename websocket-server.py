#!/usr/bin/env python

import asyncio
import websockets
from sys import stdout

async def echo(websocket, path):
    while True:
        name = await websocket.recv()
        print("< {}".format(name))

        greeting = "> {}".format(name)
        await websocket.send(greeting)
        print("> {}".format(greeting))

start_server = websockets.serve(echo, 'localhost', 5678)

print("Serving on port 5678");
stdout.flush()

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
