from LiczbyZespolone import Complex


def main():
    first, operator, second = input("Enter equation in form of complex numbers (e.g. (1,0) + (3,1)): ").split(' ')

    first = first.replace('(', ' ')
    first = first.replace(')', ' ')
    f_real, f_imag = first.split(",")

    second = second.replace('(', ' ')
    second = second.replace(')', ' ')
    s_real, s_imag = second.split(",")

    f_parsed = Complex(int(f_real), int(f_imag))
    s_parsed = Complex(int(s_real), int(s_imag))

    if operator == "+":
        result = Complex.__add__(f_parsed, s_parsed)
        print(Complex.__str__(result))
    elif operator == "-":
        result = Complex.__sub__(f_parsed, s_parsed)
        print(Complex.__str__(result))
    elif operator == "*":
        result = Complex.__mul__(f_parsed, s_parsed)
        print(Complex.__str__(result))
    elif operator == "/":
        if int(s_real != 0 and s_imag != 0):
            result = Complex.__truediv__(f_parsed, s_parsed)
            print(Complex.__str__(result))
        else:
            print("Error")


if __name__ == "__main__":
        main()
