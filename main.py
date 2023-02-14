import math
import sys


if len(sys.argv) >= 3:
    print(math.sqrt(int(sys.argv[1])**2 + int(sys.argv[2])**2))
else:
    print("hello")