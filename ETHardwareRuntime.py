import asyncio, configparser, json, os, socket, threading, time, urllib.request, websockets, pyusb, argpass
from websockets.server import WebSocketServerProtocol as wetSocks

# Eye Tracker Hardware Runtime | Cross platform Runtime for Eye Tracking Hardware

# Hardware Defines (USB)

ET5 = {
"Device Name": "Tobii Eye Tracker 5",
"USBVID": "0x2104",
"USBPID": "0x0313"
}


# main
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--device", help="Device Select")

print(f"ETHardwareRuntime")



# Hopeful  Data output:
gaze_x = 0 # Expected to be 0-1 (Left to Right)
gaze_y = 0 # Expected to be 0-1 (Bottom to Top)

gaze_point = { gaze_x, gaze_y }

LE_X = 0 # Left Eye X coordinate
LE_Y = 0 # Left Eye Y coordinate
LE_Z = 0 # Left Eye Z coordinate

RE_X = 0 # Right Eye X coordiante
RE_Y = 0 # Right Eye X coordiante
RE_Z = 0 # Right Eye X coordiante

Left_Eye_Origin = { LE_X, LE_Y, LE_Z ) # Left eye position
Right_Eye_Origin = { RE_X, RE_Y, RE_Z ) # Right eye position

Head_X = 0 # Estimated Rotation 0-180 degrees
Head_Y = 0 # Estimated Rotation 0-180 degrees
Head_Z = 0 # Estimated Rotation 0-180 degrees

Head_Rotation = { Head_X, Head_Y, Head_Z } # Head Rotation in an array ready for use
