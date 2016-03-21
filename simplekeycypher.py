import sys
import random

mFileName = sys.argv[1]

mFile = open(mFileName, "r").read()
ABC = "abcdefghijklmnopqrstuvwxyz"
r_ABC = "abcdefghijklmnopqrstuvwxyz"[::-1]

f = str.split(mFile, "\n")
strs = []
for i in f:
    if len(i) > 1:
        strs.append(i)
msgs = []
ks = []
for s in strs:
    s = s.replace(" ", "")
    string = ""
    key = ""
    for i in range(len(s)):
        k = random.randrange(0, 16)
        index = ABC.index(s[i])
        newChar = ABC[(index + k) % len(ABC)]
        key += str(k) + " "
        string += newChar
    msgs.append(string)
    key = key[0:len(key)-1]
    ks.append(key)
print(msgs)
print(ks)
kfile = open(str.split(mFileName, ".")[0] + ".key", "w")
for i in ks:
    kfile.write(i + "\n")

cfile = open(str.split(mFileName, ".")[0] + ".cypher", "w")
for i in msgs:
    cfile.write(i + "\n")
