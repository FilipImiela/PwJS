import math as m


def main():
    a = int(input("First coefficient: "))
    b = int(input("Second coefficient: "))
    c = int(input("Third coefficient: "))

    delta = (b*b)-(4*a*c)
    if delta > 0:
        x1 = (-b-m.sqrt(delta))/(2*a)
        x2 = (-b+m.sqrt(delta))/(2*a)
        print("x1=", x1, "x2=", x2)
    elif delta == 0:
        x0 = -b/(2*a)
        print("One root: x0= ", x0)
    else:
        print("No roots!")


if __name__ == "__main__":
    main()