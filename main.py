import math
mat = input("+ - / * sqrt more:")
if mat == "more":
    mat = input("area, circum, log: ")
    if mat == "area":
        mat = (input("circle, triangle: "))
        if mat == "circle":
            mat = int(input("Radius: "))
            print(math.pi*(mat**2))
    if mat == "triangle":
        number1 = int(input("Base: "))
        number2 = int(input("Height: "))
        print(number1*number2/2)
    if mat == "circum":
        mat = int(input("radius: "))
        print(2 * math.pi * mat)
    if mat == "log":
        base = int(input("Base: "))
        exponent = int(input("Exponent: "))
        print(math.log(base**exponent) / math.log(base))
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
