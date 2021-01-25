import random
def main():
    rand_tab =[]
    for i in range(0, 49):
        x = random.randint(0, 50)
        rand_tab.append(x)

    print("Rand tab: \n", rand_tab)

    rand_tab.sort()
    rand_tab.reverse()
    print("Sorted with built-in funtion: \n", rand_tab)

    n = len(rand_tab)

    for i in range(n-1):
        for j in range(n-i-1):
            if rand_tab[j] < rand_tab[j+1]:
                rand_tab[j], rand_tab[j+1] = rand_tab[j+1], rand_tab[j]

    print("Sorted: \n", rand_tab)

if __name__ == "__main__":
    main()