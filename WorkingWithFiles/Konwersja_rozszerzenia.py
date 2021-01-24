import os
from PIL import Image


def main():
    path = "."
    files = os.listdir(path)
    for i in range(len(files)):
        if files[i].endswith(".jpg"):
            im = Image.open(files[i]).convert("RGB")
            files[i] = files[i].replace(".jpg", ".png")
            im.save(files[i], "png")


if __name__ == "__main__":
    main()
