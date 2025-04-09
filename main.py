from microbit import *
def number_algorithm():
    pin = ""
    while len(pin) < 4:
        number = 0
        start_time = running_time()
        while running_time() - start_time < 5000:
            if button_a.was_pressed():
                number += 1
                display.show(str(number))
                sleep(200)
            elif button_b.was_pressed():
                number -= 1
                display.show(str(number))
                sleep(200)
            sleep(50)
        pin += str(number)
        display.scroll("PIN:" + pin)
    return int(pin)

def checking_return():
    missing_key = []
    for key, val in key_pin_system.items():
        if (val[1] == True):
            # represents it's not returned back
            missing_key.append(key)

    return missing_key

key_pin_system = {}
def getting_system():
    with open("system.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            key, value = line.split(", ")
            key_pin_system[key] = [int(value), False]

def check_pin(entered):
    for val in key_pin_system.values():
        if entered == val[0]:
            if val[1] == True:
                print("Unbrella already been borrowed, plz returned back!")
                return False
            else:
                val[1] = True
                return True
    return False

cur = running_time()  # Set the base time before entering the loop
getting_system()
while True:
    # borrow umbrella if button A is pressed, etc.
    if button_a.was_pressed():
        pin = number_algorithm()
        if check_pin(pin):
            display.show(Image.HAPPY)
        else:
            display.show(Image.NO)
    # elif button_b.was_pressed():

    if running_time() - cur > 10000:
        # 2 minutes have passed; perform your daily check
        missing_person = checking_return()
        for person in missing_person:
            del key_pin_system[person]

        # Rewrite the system file with updated keys
        # with open("system.txt", "w") as f:
        #     for key, val in key_pin_system.items():
        #         f.write(f"{key}, {val[0]}\n")

        # Reset the timer or update 'cur' for the next 2 minute interval
        cur = running_time()

    sleep(50)