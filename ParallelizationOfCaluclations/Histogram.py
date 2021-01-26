import cv2
from threading import Thread
from matplotlib import pyplot as plt


def histogram(data, channel, hist):
    hist[channel] = cv2.calcHist([data], [channel], None, [256], [0, 256])


def main():
    imagfile = 'Example1.jpg'
    img = cv2.imread(imagfile, -1)
    cv2.imshow(imagfile, img)
    color = ('r', 'g', 'b')
    hist = [0] * len(color)
    threads = list()
    for index in range(len(color)):
        x = Thread(target=histogram, args=(img, index, hist))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
        plt.plot(hist[index], color=color[index])

    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()