#calculator
#choosing the numbers
number1 = float(input("what number would u like to use: "))
number2 = float(input("what other number would u like to use: "))

#choosing the functions

function1 = input("what would u like to do?  +,-,x,/ ")

if function1 == '+':
    print(number1, '+', number2,'=', number1 + number2)
elif function1 == '-':
    print(number1, '-', number2,'=',number1 - number2)
elif function1 == 'x':
    print(number1, '*', number2,'=',number1 * number2)
elif function1 == '/':
    print(number1,'/', number2,'=',number1 / number2)
