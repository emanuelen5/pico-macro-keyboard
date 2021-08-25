import board
import digitalio

btn1 = digitalio.DigitalInOut(board.GP0)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP1)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btns = [btn1, btn2]

