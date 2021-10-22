def run(a,b):
    if a == 0:
        raise ValueError("Wrong value for a")
    elif b == 0:
        raise ValueError("can't divide")

    else:
        print("Result of Division: " + str(a/b))

try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    run(a,b)

except ValueError as x:
    print(x)
except:
    print("something is wrong")
