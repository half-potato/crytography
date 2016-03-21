import random
import sys

ABC = "abcdefghijklmnopqrstuvwxyz"
strings = []
for arg in sys.argv:
    try:
        strings.append(open(arg, "r").read())
    except Exception, e:
        print e

keys = []
msgs = []
for i in strings:
    key = ""
    msg = ""
    for r in range(len(i)):
        k = random.random(26)
        key = key + str(k)
        

        with open("key.txt", "w") as text_file:
            text_file.write(key)
