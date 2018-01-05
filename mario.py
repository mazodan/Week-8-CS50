import cs50

def main():
    height = 0

    while True:
        print("Height: ", end="")
        height = cs50.get_int()
        if height < 24 and height > 0:
            break

    count = 1

    for i in range(height, 0, -1):
        for j in range((i - 1), 0, -1):
            print(" ", end="")

        print_hash(count)
        print(" ", end="")
        print_hash(count)
        print()
        count += 1

def print_hash(n):
    for i in range(n):
        print("#", end="")

if __name__ == "__main__":
    main()