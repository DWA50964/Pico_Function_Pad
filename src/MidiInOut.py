import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import usb_midi
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=1)
midiIn = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0)


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
    btnHold[btns_List.index(btn)] = False







while True:
    for btn in btns_List:
        if (not btn.value) and btnHold[btns_List.index(btn)] == False:
            midi.send(NoteOn(int(btns_List.index(btn)), 120))
            btnHold[btns_List.index(btn)] = True
        elif (btn.value) and btnHold[btns_List.index(btn)] == True:
            midi.send(NoteOff(int(btns_List.index(btn)), 120))
            btnHold[btns_List.index(btn)] = False

    msg = midiIn.receive()
    if msg is not None:
        if isinstance(msg, NoteOn):
            print(str(msg.note) + "On")
            leds_List[msg.note - 1].value = True

        else:
            print(str(msg.note) + "Off")
            leds_List[msg.note - 1].value = False








