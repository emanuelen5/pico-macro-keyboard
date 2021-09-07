"""
boot.py file for Pico data logging example. If pin GP0 is connected to GND when
the pico starts up, make the filesystem writeable by CircuitPython.
"""
import board
import digitalio
import storage
from buttons import btns, pins, CONFIG_BUTTON
import sys

print(f"Checking that no buttons are pressed at boot.")

# If write pin is connected to ground on start-up, CircuitPython can write to CIRCUITPY filesystem.
if not CONFIG_BUTTON.value:
    print("Mounting as read-only for host! Disabling storage and serial port.")
    storage.remount("/", readonly=False)
    storage.disable_usb_drive()
    usb_cdc.disable()
elif not all(btn.value for btn in btns):
    print("Not all buttons were 'up'. Exiting")
    sys.exit(-1)
else:
    print("Not pressed. Starting in RW mode.")
