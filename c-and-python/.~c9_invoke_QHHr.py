# Also demonstrates bypassing the newline in print
import cs50

print("x is", end="")
x = cs50.get_int()

print("y is", end="")
y = cs50.get_int()

print("{} plus {} is {}".format(x, y, x + y))
print("{} minus {} is {}".format(x, y, x - y))
print("{} times {} is {}".format(x, y, x * y))
print("{} divided by {} is {}".format(x, y, x / y))
print("{} divided by {} and floored is {}".format(x, y, x // y))
print("remainder of {} divided by {} is {}".format(x, y, x % y))