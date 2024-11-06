systems_size = "0123456789ABCDEF"

def decimal_to_binary(number: int) -> str:
    output = ""
    while number != 1:
        output += str(number % 2)
        number = number // 2
    output += str(number % 2)
    return "0b" + str(output[::-1])

def decimal_to_hexadecimal(number: int) -> str:
    output = ""
    while number >= 16:
        output += systems_size[number % 16]
        number = number // 16
    output += systems_size[number % 16]
    return "0x" + str(output[::-1])

def decimal_to_any(number: int, size: int) -> str:
    if size < 2 or size > len(systems_size):
        return "Please enter a size from 2-16"
    output = ""
    while number >= size:
        output += systems_size[number % size]
        number = number // size
    output += systems_size[number % size]
    return str(output[::-1]) + f"x{size}"

def any_to_decimal(any: str) -> int:
    output = 0
    any = any.split("x")
    any[0] = any[0][::-1]
    for i in range(len(any[0])):
        output += systems_size.index(any[0][i]) * int(any[1]) ** i
    return output

def binary_to_decimal(binary: str) -> str:
    output = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            output += 2**i
    return str(output)

def hexadecimal_to_decimal(hexadecimal: str) -> str:
    output = 0
    hexadecimal = hexadecimal[::-1]
    for i in range(len(hexadecimal)):
        output += systems_size.index(hexadecimal[i]) * 16 ** i
    return str(output)

def cycle(option:str , number: str) ->str:
    if option == "1":
        return decimal_to_binary(int(number))
    if option == "2":
        return decimal_to_hexadecimal(int(number))
    if option == "3":
        return binary_to_decimal(number)
    if option == "4":
        return hexadecimal_to_decimal(number)

while True:
    option = input("Choose an option you want to do:\n"
                   "1. Decimal to binary\n"
                   "2. Decimal to hexadecimal\n"
                   "3. Decimal to any\n"
                   "4. Binary to decimal\n"
                   "5. Hexadecimal to decimal\n"
                   "6. Any to decimal\n"
                   "7. Exit\n"
                   ">>> ")  
    if option == '7':
        print("Thanks for using")
        break
    inp = input("Please enter a number in the system you chosen: ")

    print(cycle(option, inp))