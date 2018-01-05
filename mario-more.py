import cs50

height = 0

while True:
    print("Height: ", end="")
    height = cs50.get_int()
    if height < 24 and height > 0:
        break

stairs = 2

for i in range(height, 0, -1):
    for j in range((i - 1)):
        print(" ", end="")

    for k in range(stairs, 0, -1):
        print("#", end="")

    stairs += 1
    print()