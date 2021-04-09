import random


def primary():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    for i in range(3):
        rnd = random.randint(0, len(quotes)-1)
        print(quotes[rnd])

    g = open("quotes_.txt", "w")
    g.write("ayano desitawa.")
    g.close()


if __name__ == "__main__":
    primary()
