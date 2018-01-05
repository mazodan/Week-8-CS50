import cs50
import math

def main():
    print("O hai! How much change is owed?")
    cash = cs50.get_float()

    while cash < 0:
        print("How much change is owed?")
        cash = cs50.get_float()

    cents = round(cash * 100)

    counter = 0

    if cents >= 25:
        counter += incrementCounter(cents, 25)
        cents %= 25

    if cents >= 10:
        counter += incrementCounter(cents, 10)
        cents %= 10

    if cents >= 5:
        counter += incrementCounter(cents, 5)
        cents %= 5

    if cents >= 1:
        counter += incrementCounter(cents, 1)
        cents %= 1

    print("{}".format(counter))

def incrementCounter(cents, unit):
    return math.floor(cents / unit)

if __name__ == "__main__":
    main()