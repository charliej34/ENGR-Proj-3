pin_system = {}
while True:
    username = input("Enter your Purdue username: ")
    set = False
    while not set:
        try:
            pin_number = input("Enter your pin number: ")
            if (len(pin_number) < 4):
                print("Length must be 4! Try it again!")
            pin = int(pin_number)
            if pin > 0 and pin < 9999 and pin not in pin_system.values():
                set = True
            else:
                print("pin number exceeding the valid ranges or existing in the system! Try it again!")
        except ValueError:
            print("Invalid pin number setting, please try it again")

    pin_system[username] = pin

    end = input("Wanna end? ")
    if end == "Y":
        break


with open("system.txt", "w") as f:
    for key, value in pin_system.items():
        f.write(f"{key}, {value}\n")
