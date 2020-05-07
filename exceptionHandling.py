

try:
    a = int(input("enter first number to divide"))
    b = int(input("enter second number to divide"))
    c = a / b
    print(c)

except ZeroDivisionError as e:
    print("Hey you cannot divide by number 0", e)

except ValueError as e:
    print("Hey please give number to divide", e)

finally:
    print("In Finally block")
