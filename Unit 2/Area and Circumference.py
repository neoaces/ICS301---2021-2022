if __name__ == "__main__":
    MODE = str()
    input_received = False


    def AREA(r: float) -> float:
        return 3.1415 * (r ** 2)


    def CIRC(r: float) -> float:
        return (2 * 3.1415) * r


    while not input_received:
        buffer = str(input("What mode would you like to operate in?\n A - Area\n C - Circumference\n"))

        if buffer == "A":
            MODE = "A"
            input_received = True

        if buffer == "C":
            MODE = "C"
            input_received = True

    radius = float(input("What is your radius? "))

    if MODE == "A":
        print("Your area is: " + str(AREA(radius)))
    elif MODE == "C":
        print("Your radius is: " + str(CIRC(radius)))
