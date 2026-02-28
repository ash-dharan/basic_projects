def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1/num2

def exponent(num1,num2):
    return num1**num2

def floordiv(num1,num2):
    return num1//num2

def modulo(num1,num2):
    return num1%num2

history = []



def main():
    print("== CLI Calculator ==\n")
    while True:
        try:
            num1 = float(input("Enter a number: "))
            op = input("Enter a operator (+, -, *, /, **, //) : ")
            num2 = float(input("Enter a number: "))
            result = None

        
            if op == "+":
                result = add(num1,num2)
            elif op == "-":
                result = sub(num1,num2)
            elif op == "*":
                result = mult(num1,num2)
            elif op == "/":
                result = divide(num1,num2)
            elif op == "**":
                result = exponent(num1,num2)
            elif op == "//":
                result = floordiv(num1,num2)
            elif op == "%":
                result = modulo(num1,num2)
            else:
                print("Please enter a specified operator")

            history.append(f"{num1} {op} {num2} = {result}")

            print(f"{result}")
        except ValueError:
            print("Please enter a numeric value")

        
        choice = input("Do you want to calculate again? (y/n)").lower()
        if choice != "y":
            print("Goodbye!")
            break
    
if __name__ == "__main__" :
     main()
    



