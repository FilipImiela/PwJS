import os


def list_files(path):
    for file in os.listdir(path):
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            print(new_path)
            list_files(new_path)


def main():

    path = '.'
    list_files(path)


if __name__ == "__main__":
    main()
