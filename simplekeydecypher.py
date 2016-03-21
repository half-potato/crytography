import sys
import random

mFileName = sys.argv[1]
kFileName = sys.argv[2]

mFile = open(mFileName, "r").read()
shift = open(kFileName, "r").read()
ABC = "abcdefghijklmnopqrstuvwxyz"
r_ABC = "abcdefghijklmnopqrstuvwxyz"[::-1]

strs = str.split(mFile, "\n")
msgs = []
ks = str.split(shift, "\n")
for x in range(len(strs)):
    s = strs[x].replace(" ", "")
    key = str.split(ks[x], " ")
    string = ""
    for i in range(len(s)):
        k = -int(key[i])
        index = ABC.index(s[i])
        newChar = ABC[(index + k) % len(ABC)]
        string += newChar
    msgs.append(string)

print(msgs)
