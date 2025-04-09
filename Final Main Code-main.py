from microbit import *
import robotbit_library as r

setting_pin = True
entered_pin = []
stored_pin = []
unlocked = False

M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

r.setup()

def input_loop(prompt):
    pin = []
    display.scroll(prompt)
    while len(pin) < 4:
        if button_a.was_pressed():
            pin.append('A')
            display.show('A')
            sleep(500)
            display.clear()
        elif button_b.was_pressed():
            pin.append('B')
            display.show('B')
            sleep(500)
            display.clear()
    return pin

def check_pin(entered, stored):
    return entered == stored

def lockDoor():
    r.motor(M2A, 50)
    r.sleep(200)
    r.motor_stop(M2A)
    

def unlockDoor():
    r.motor(M2A, 50)
    r.sleep(200)
    r.motor_stop(M2A)

while True:
    if setting_pin:
        stored_pin = input_loop("Set PIN")
        display.show(Image.YES)
        sleep(1000)
        display.clear()
        setting_pin = False
    elif not unlocked:
        entered_pin = input_loop("Enter PIN")
        if check_pin(entered_pin, stored_pin):
            display.show(Image.HAPPY)
            unlocked = True
        else:
            display.show(Image.NO)
        sleep(1000)
        display.clear()
    else:
        display.scroll("Unlocked")
        sleep(3000)
        unlocked = False 