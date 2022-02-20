import sys



try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x/y
except (ZeroDivisionError, ValueError):
    print("Error: Cannot Divide")
    sys.exit(1)

print(f"The result is : {result}")