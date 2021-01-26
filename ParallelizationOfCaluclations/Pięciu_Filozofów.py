import time
import threading


class Philosopher(threading.Thread):
    flag = True

    def __init__(self, index, leftF, rightF):
        threading.Thread.__init__(self)
        self.index = index
        self.leftF = leftF
        self.rightF = rightF

    def run(self):
        while self.flag:
            time.sleep(7)
            print('No. %s wants to eat.' % self.index)
            self.dine()

    def dine(self):
        fork1, fork2 = self.leftF, self.rightF
        while self.flag:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print('No. %s swaps forks.' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print('No. %s starts eating. ' % self.index)
        time.sleep(7)
        print('No. %s finishes eating.' % self.index)


def main():
    forks = [threading.Semaphore() for n in range(5)]
    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]
    Philosopher.flag = True
    for i in range(5):
        philosophers[i].start()

    time.sleep(25)

    Philosopher.flag = False
    print("Finishing.")


if __name__ == "__main__":
    main()
