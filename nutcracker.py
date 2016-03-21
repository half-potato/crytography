import sys

f = open(sys.argv[1], "r")

lines = str.split(f, "\n")
for i in range(len(lines)):
    lines[i] = lines[i].replace(" ", "")
    lines[i] = lines[i].lower()

ABC = "abcdefghijklmnopqrstuvwxyz"

def shift(char, shift):
    return ABC[ABC.index(char) + shift]

msgs = ""
for i in range(26):
    for l in lines:
        line = ""
        for c in l:
            line += shift(c, i)
