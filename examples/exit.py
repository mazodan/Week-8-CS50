import cs50
import sys
# Demonstrates exit codes in python
if len(sys.argv) != 2:
    print("Missing command line argument")
    exit(1)

print("Hello, {}".format(sys.argv[1]))
exit(0)