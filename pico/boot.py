"""
boot.py file for Pico data logging example. If pin GP0 is connected to GND when
the pico starts up, make the filesystem writeable by CircuitPython.
"""
import board
import digitalio
import storage
from buttons import btns, pins

print(f"Checking if btn[0]={pins[0]} is pressed.")

# If write pin is connected to ground on start-up, CircuitPython can write to CIRCUITPY filesystem.
if not btns[0].value:
    print("Mounting as read-only for host! Disabling storage and serial port.")
    storage.remount("/", readonly=False)
    storage.disable_usb_drive()
    usb_cdc.disable()
else:
    print("Not pressed. Starting in RW mode.")
