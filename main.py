import math
mat = input("+ - / * sqrt more:")
if mat == "more":
    mat = input("area, circ: ")
    if mat == "area":
        mat = int(input("radius: "))
        print(math.pi*(mat**2))
    if mat == "circ":
        print("L BOZO")
else:
    if mat == "sqrt":
        numbersqrt = int(input("Numbersqrt:"))
        print(math.sqrt(numbersqrt))
    if mat != "sqrt":
        number1 = int(input("Number1:"))
        number2 = int(input("Number2:"))
    if mat == "+":
        print(number1 + number2)
    if mat == "-":
        print(number1 - number2)
    if mat == "/":
        print(number1 / number2)
if mat == "*":
    print(number1 * number2)
