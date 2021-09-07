import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio
import json
import sys
from buttons import btns, pins, CONFIG_BUTTON
BUTTON_COUNT = len(btns)

print("Starting")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

key_combos = [[None]] * BUTTON_COUNT
key_names = [""] * BUTTON_COUNT

keyboard = Keyboard(usb_hid.devices)


if not CONFIG_BUTTON.value:
    print("Don't care about the config button. It only has special meaning for the boot script.")
if not all(btn.value for btn in btns):
    print("Not all buttons were 'up'. Exiting")
    sys.exit(-1)

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
    print(f"Configuring key {i+1} ({pins[i]})")
    keys = config[i]
    if keys is None:
        key_names[i] = "None"
        key_combos[i] = None
    else:
        key_names[i] = " + ".join(keys)
        keys = [str2key(k) for k in keys]
        key_combos[i] = keys
    print(f"  Got: {key_names[i]} = {keys}")


KEY_TIMEOUT = 0.2 # The time after a key is repeated when held down
USB_KEY_MIN_TIME = 0.02 # The time between sending muxed keys to host
last_button_press_time = 0
button_pressed_flags = [False] * BUTTON_COUNT
button_last_sent_time = [0] * BUTTON_COUNT
current_key_index = 0


# Main loop
while True:
    t = time.monotonic()
    led.value = int(t) % 2
    for i, btn in enumerate(btns):
        if not btn.value:  # Low -> pressed
            # Check for timeout on individual buttons
            if not button_pressed_flags[i] and t > button_last_sent_time[i] + KEY_TIMEOUT:
                button_pressed_flags[i] = True
                print(f"Setting flag for key{i}", button_last_sent_time[i], t + KEY_TIMEOUT)

    # Round robin checking
    if not button_pressed_flags[current_key_index]:
        current_key_index = (current_key_index + 1) % BUTTON_COUNT
    # If pressed, check that at least the time has passed
    elif t > (last_button_press_time + USB_KEY_MIN_TIME):
        keys = key_combos[current_key_index]
        name = key_names[current_key_index]
        if keys is None:
            print(f"Button {current_key_index} pressed, but not configured.")
        else:
            print(f"Button {current_key_index} pressed. Sending keys {name}")
            keyboard.send(*keys)
            last_button_press_time = time.monotonic()
        button_last_sent_time[current_key_index] = time.monotonic()
        button_pressed_flags[current_key_index] = False
        current_key_index = (current_key_index + 1) % BUTTON_COUNT

