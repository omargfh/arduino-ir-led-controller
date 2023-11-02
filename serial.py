from time import sleep
import serial.tools.list_ports
from flask import Flask, request, jsonify
from flask_cors import CORS
import math

ports = list(serial.tools.list_ports.comports())
serialInst = serial.Serial()

_ = [print(f"{i}. {port}") for i, port in enumerate(ports)]
print("Enter the port number: ", end="")
try:
    port_number = int(input())
    print(f"Selected port: {port_number}")
    port = ports[port_number]
except:
    print("Invalid port number!")
    exit()

serialInst.baudrate = 115200
serialInst.port = port.device
serialInst.open()

print("Connected to Arduino!")

REMOTE_COMMAND = {
    'BRIGHTNESS_UP': 0x5C04,
    'BRIGHTNESS_DOWN': 0x5D04,
    'PLAY': 0x4104,
    'POWER': 0x4004,
    'COLOR_RED': 0x5804,
    'COLOR_PINK': 0x5804,
    'COLOR_GREEN': 0x5904,
    'COLOR_BLUE': 0x4504,
    'COLOR_RED1': 0x5404,
    'COLOR_ORANGE': 0x5404,
    'COLOR_GREEN1': 0x5504,
    'COLOR_BLUE1': 0x5904,
    'COLOR_RED2': 0x5004,
    'COLOR_GREEN2': 0x5104,
    'COLOR_BLUE2': 0x4D04,
    'COLOR_RED3': 0x1C04,
    'COLOR_GREEN3': 0x1D04,
    'COLOR_CYAN': 0x1D04,
    'COLOR_BLUE3': 0x1E04,
    'COLOR_RED4': 0x1804,
    'COLOR_YELLOW': 0x1804,
    'COLOR_GREEN4': 0x1904,
    'COLOR_BLUE4': 0x1A04,
    'COLOR_PURPLE': 0x1A04,
    'COLOR_WHITE': 0x4404,
    'MUSIC1': 0x4804,
    'MUSIC2': 0x4C04,
    'MUSIC3': 0x1F04,
    'MUSIC4': 0x5B04,
    'AUTO': 0x1704,
    'SLOW': 0x1304,
    'QUICK': 0xF04,
    'FLASH': 0xB04,
    'JUMP3': 0x404,
    'JUMP7': 0x504,
    'FADE3': 0x604,
    'FADE7': 0x704,
    'RED_UP': 0x1404,
    'RED_DOWN': 0x1004,
    'GREEN_UP': 0x1504,
    'GREEN_DOWN': 0x1104,
    'BLUE_UP': 0x1604,
    'BLUE_DOWN': 0x1204,
    'DIY1': 0xC04,
    'DIY2': 0xD04,
    'DIY3': 0xE04,
    'DIY4': 0x804,
    'DIY5': 0x904,
    'DIY6': 0xA04
}

def command(color):
    return (REMOTE_COMMAND[color.upper()] if color.upper() in REMOTE_COMMAND else REMOTE_COMMAND["COLOR_WHITE"]) + 4

def send(color):
    serialized_cmd = command(color)
    bytes = serialized_cmd.to_bytes(4, byteorder="little")
    serialInst.write(bytes)

app = Flask(__name__)
CORS(app)

known_colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "green": (191, 255, 92),
    "blue": (0, 0, 255),
    "blue": (22, 31, 80),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "cyan": (0, 255, 255),
    "pink": (255, 192, 203),
    "purple": (128, 0, 128),
    "purple": (82, 104, 229),
    "white": (255, 255, 255),
    "red2": (139, 69, 19),
}

def color_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def max_color_brightness(color):
    r, g, b = color
    maxB = max(r, g, b)
    multiplier = 255 // maxB
    return (r * multiplier, g * multiplier, b * multiplier)

def closest_color(hex_color):
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    r, g, b = max_color_brightness((r, g, b))
    closest = None
    min_distance = float('inf')

    for color_name, color_values in known_colors.items():
        distance = color_distance((r, g, b), color_values)
        if distance < min_distance:
            min_distance = distance
            closest = color_name

    return closest

@app.route("/set", methods=["GET"])
def set():
    hex = request.args.get("hex")
    color = "color_" + closest_color("#"+hex)
    send(color)
    sleep(.05)
    send(color)
    print(color)
    return jsonify({"status": "ok", "color": color})

@app.route("/strset", methods=["GET"])
def strset():
    color = request.args.get("color")
    color = "color_" + color
    send(color)
    sleep(.05)
    send(color)
    return jsonify({"status": "ok", "color": color})

app.run(host='0.0.0.0', port=8080)
