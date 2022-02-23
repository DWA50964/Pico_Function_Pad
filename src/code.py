import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

#Setup Keyboard HID Device
time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

#Led Setup
led1 = digitalio.DigitalInOut(board.GP2)
led2 = digitalio.DigitalInOut(board.GP8)
led3 = digitalio.DigitalInOut(board.GP28)
led4 = digitalio.DigitalInOut(board.GP5)
led5 = digitalio.DigitalInOut(board.GP3)
led6 = digitalio.DigitalInOut(board.GP26)
led7 = digitalio.DigitalInOut(board.GP15)

#Assigns all the LEDs as GPIO inputs
leds_List = [led1, led2, led3, led4, led5, led6, led7]
for led in leds_List:
    led.direction = digitalio.Direction.OUTPUT


#Button Setup
btn1 = digitalio.DigitalInOut(board.GP11)
btn2 = digitalio.DigitalInOut(board.GP10)
btn3 = digitalio.DigitalInOut(board.GP22)
btn4 = digitalio.DigitalInOut(board.GP12)
btn5 = digitalio.DigitalInOut(board.GP20)
btn6 = digitalio.DigitalInOut(board.GP19)
btn7 = digitalio.DigitalInOut(board.GP14)
btn8 = digitalio.DigitalInOut(board.GP13)
btn9 = digitalio.DigitalInOut(board.GP18)
btn10 = digitalio.DigitalInOut(board.GP17)

#Sets up mode button as input
btnFn = digitalio.DigitalInOut(board.GP16)
btnFn.direction = digitalio.Direction.INPUT
btnFn.pull = digitalio.Pull.UP

#A dictionary to hold a count of how long each button is held
btnHold = {}

#Assigns the buttons as GPIO Inputs
btns_List = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10]
for btn in btns_List:
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    btnHold[btns_List.index(btn)] = 0




global mode
global modeList
global functionKeys

#List of all modes in use
modeList = [0,1,2,3,10]

#List of Hidden Function Key Key Codes
functionKeys = [Keycode.F13, Keycode.F14,Keycode.F15, Keycode.F16, Keycode.F17, Keycode.F18, Keycode.F19,Keycode.F20, Keycode.F21, Keycode.F22]

def keyPress(key):
    global mode
    global modeList

    #Number pad mode
    if mode == 1:
        if int(key) < 10:
            keyboard_layout.write(str(key))
        else:
            keyboard_layout.write("0")
        time.sleep(0.1)

    #Functions Keys Mode
    if mode == 2:
        keyboard.press(functionKeys[int(key)-1])
        keyboard.release_all()
        time.sleep(0.1)

    #Programming Shortcuts
    if mode == 3:
        if int(key) == 1:
            keyboard.press(Keycode.CONTROL, Keycode.C)
            keyboard.release_all()
        if int(key) == 2:
            keyboard.press(Keycode.CONTROL, Keycode.X)
            keyboard.release_all()
        if int(key) == 3:
            keyboard.press(Keycode.CONTROL, Keycode.V)
            keyboard.release_all()

        if int(key) == 4:
            keyboard_layout.write("(")
            keyboard.release_all()

        if int(key) == 5:
            keyboard_layout.write("()")
            keyboard.release_all()
            keyboard.press(Keycode.LEFT_ARROW)
            keyboard.release_all()

        if int(key) == 6:
            keyboard_layout.write(")")
            keyboard.release_all()

        if int(key) == 7:
            keyboard_layout.write("[")
            keyboard.release_all()

        if int(key) == 8:
            keyboard_layout.write("[]")
            keyboard.release_all()
            keyboard.press(Keycode.LEFT_ARROW)
            keyboard.release_all()

        if int(key) == 9:
            keyboard_layout.write("]")
            keyboard.release_all()

        if int(key) == 10:
            keyboard.press(Keycode.CONTROL, Keycode.S)
            keyboard.release_all()
        time.sleep(0.1)

    #Led Test Mode
    if mode == 10:
        for led in leds_List:
            led.value = True
            time.sleep(0.2)
        for led in leds_List:
            led.value = False
            time.sleep(0.2)

    #Mode Selection mode
    if mode == 0:
        if int(key) in modeList:
            mode = int(key)
            #Blinks Leds to mark Selected mode
            for i in range(mode):
                for led in leds_List:
                    led.value = True
                time.sleep(0.2)
                for led in leds_List:
                    led.value = False
                time.sleep(0.2)


#Boot Lights
for led in leds_List:
    led.value = True
    time.sleep(0.2)
for led in leds_List:
    led.value = False
    time.sleep(0.2)

#Default mode
mode = 1
count = 0


#Main Program Loop
while True:

    #Checks for button presses
    for btn in btns_List:
        if not btn.value:
            #Checks to see if key is being held to present unwanted extra key strokes.
            if (btnHold[btns_List.index(btn)] < 1 or btnHold[btns_List.index(btn)] > 1500):
                keyPress(str(btns_List.index(btn) + 1))
            btnHold[btns_List.index(btn)] += 1
        else:
            btnHold[btns_List.index(btn)] = 0




    #Checks for function button presses
    if not btnFn.value:
        led7.value = True
        count += 1

    #If function button is tapped, blink to show modes
    else:
        led7.value = False
        if count > 10:
            time.sleep(0.4)
            for i in range(mode):
                led7.value = True
                time.sleep(0.2)
                led7.value = False
                time.sleep(0.2)
        count = 0

    #If function button is held enter mode selection
    if count == 3000:
        mode = 0
        led7.value = False
        time.sleep(1)
        for i in range(2):
            for led in leds_List:
                led.value = True
            time.sleep(0.2)
            for led in leds_List:
                led.value = False
            time.sleep(0.2)
        count = 0


