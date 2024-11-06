
def decimal_to_binary(number: int) -> str:
    output = ""
    while number != 1:
        output += str(number % 2)
        number = number // 2
    output += str(number % 2)
    return "0b" + str(output[::-1])

def binary_to_decimal(binary: str) -> int:
    output = 0
    binary = binary[2:][::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            output += 2**i
    return output

def cycle(number:str ) ->str:
    if number[:2] == "0b":
        return str(binary_to_decimal(number))
    return decimal_to_binary(int(number))

while True:
    inp = input("Enter a number: ")
    print(cycle(inp))