import board
import digitalio

pins = [board.GP0, board.GP1]
btns = []
for pin in pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    btns.append(btn)
