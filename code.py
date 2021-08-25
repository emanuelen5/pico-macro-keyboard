import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio
import json

print("Starting")

btn1 = digitalio.DigitalInOut(board.GP0)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP1)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

btns = [btn1, btn2]
BUTTON_COUNT = len(btns)
key_combos = [[None]] * BUTTON_COUNT
key_names = [""] * BUTTON_COUNT

keyboard = Keyboard(usb_hid.devices)

try:
    with open("config.json", "rt") as f:
        config = json.load(f)
except ValueError as e:
    print(e)
    print("Could not load JSON configuration file 'config.json'")


def str2key(key: str):
    if not isinstance(key, str):
        raise ValueError(f"Not a string. Got {key}.")
    try:
        k = getattr(Keycode, key)
    except AttributeError:
        raise ValueError(f"'{key}' is not a valid keycode.")
    return k


for i in range(BUTTON_COUNT):
    print(f"Getting config for item {i}")
    keys = config[i]
    if keys is None:
        key_names[i] = "None"
        key_combos[i] = None
        continue
    key_names[i] = " + ".join(keys)
    keys = [str2key(k) for k in keys]
    key_combos[i] = keys

while True:
    t = time.time()
    led.value = t % 2
    for i, (key, name, btn) in enumerate(zip(key_combos, key_names, btns)):
        if not btn.value:  # Low -> pressed
            if key is None:
                print(f"Button {i} pressed, but not configured.")
            else:
                print(f"Button {i} pressed. Sending keys {name}")
                keyboard.send(*key)
            time.sleep(0.2)

