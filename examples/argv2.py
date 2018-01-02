# demonstrates foreach loop in python

import sys

for s in sys.argv:
    for c in s:
        print(c)
    print()