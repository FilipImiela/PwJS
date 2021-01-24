
def main():
    arch = 1234
    print("Enter code: ")
    code = int(input())
    while code != arch:
        print("Wrong code! Please try again: ")
        code = int(input())
    print("Match!")

if __name__ == "__main__":
    main()