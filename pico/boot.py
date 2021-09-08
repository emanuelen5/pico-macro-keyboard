"""
If a key is connected to GND when the pico starts up, make the filesystem writeable by host (for configuring/reprogramming).
"""
import board
import digitalio
import storage
from buttons import btns, pins, CONFIG_BUTTON
import sys

print(f"Checking that no buttons are pressed at boot.")

# If write pin is connected to ground on start-up, CircuitPython can write to CIRCUITPY filesystem.
if not all(btn.value for btn in btns):
    print("Not all buttons were 'up'. Make sure to exit in the main script... Exiting in the boot.py-script does nothing in particular...")
    sys.exit(-1)
else:
    print("Mounting as read-only for host! Disabling storage and serial port.")
    storage.remount("/", readonly=False)
    storage.disable_usb_drive()
    usb_cdc.disable()
