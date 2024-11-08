systems_size = "0123456789ABCDEF"

def decimal_to_any(number: int, size: int) -> str:
    output = ""
    while number >= size:
        output += systems_size[number % size]
        number = number // size
    output += systems_size[number % size]
    if size == 2: return f"0b{output[::-1]}"
    if size == 16: return f"0x{output[::-1]}"
    return f"{output[::-1]}x{size}"

def any_to_decimal(anything: str, size: str) -> int:
    output = 0
    anything = anything[::-1]
    for i in range(len(anything)):
        output += systems_size.index(anything[i]) * int(size) ** i
    return output

def size_input() -> str:
    size = input("\nPlease enter a size from 2-16 of numeral system:\n"
                 ">>> ")
    while not size.isdecimal() or not (2 <= int(size) <= len(systems_size)):
        print("Invalid size")
        size = input("\nPlease enter a size from 2-16 of numeral system:\n"
                     ">>> ")
    return size
def check_number(number: str) -> str or int:
    if number.isdecimal():
        return decimal_to_any(int(number), int(size_input()))

    if number[:2] == "0b" and len(number[2:]) == len([x for x in number[2:] if x in systems_size[:2]]):
        return decimal_to_any(any_to_decimal(number[2:], "2"), int(size_input()))

    if number[:2] == "0x" and len(number[2:]) == len([x for x in number[2:] if x in systems_size]):
        return decimal_to_any(any_to_decimal(number[2:], "16"), int(size_input()))

    if (("x" in number[-2:] and number[-1] in systems_size
         and len(number[:-2]) == len([x for x in number[:-2] if x in systems_size[:int(number[-1])]]))
            or ("x" in number[-3:] and int(number[-2]) <= len(systems_size)
                and len(number[:-3]) == len([x for x in number[:-3] if x in systems_size[:int(number[-2:])]]))):

        return decimal_to_any(any_to_decimal(number.split("x")[0], number.split("x")[1]), int(size_input()))

    number = input("\nPlease enter a valid number:\n"
                   ">>> ")
    return check_number(number)

def cycle() -> None:
    while True:
        option = input("\nChoose an option you want to do:\n"
                       "1. Convert\n"
                       "2. Exit\n"
                       ">>> ")
        if option.lower() == "convert" or option.lower() == "1":
            inp = input("\nPlease enter a number:\n"
                        ">>> ")
            print(check_number(inp))
        elif option == "2" or option.lower() == "exit":
            print("Thanks for using!")
            break
        else:
            print("Please enter a valid option")

cycle()