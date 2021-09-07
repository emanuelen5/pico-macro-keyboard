import board
import digitalio

pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5]
btns = []
for pin in pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    btns.append(btn)

CONFIG_BUTTON = btns[0]
