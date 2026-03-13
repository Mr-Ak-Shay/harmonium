import asyncio
import websockets
import json

async def handler(websocket):
    print("\nWeb App connected! Move your mouse UP to pump the bellows.")
    async for message in websocket:
        try:
            data = json.loads(message)
            mouse_y = data.get("mouseY", 0.5)
            angle = (1.0 - mouse_y) * 90  # top of screen = 90°, bottom = 0°
            print(f"\rAngle: {angle:.1f}°   ", end="", flush=True)
            await websocket.send(json.dumps({"angle": angle}))
        except websockets.ConnectionClosed:
            print("\nWeb App disconnected.")
            break

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Bridge active! Waiting for your web app on port 8765...")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopping Bridge...")
