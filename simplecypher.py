import sys

mFileName = sys.argv[1]
shift = sys.argv[2]

mFile = open(mFileName, "r").read()
ABC = "abcdefghijklmnopqrstuvwxyz"
r_ABC = "abcdefghijklmnopqrstuvwxyz"[::-1]

strs = str.split(mFile, "\n")
msgs = []
for s in strs:
    s = s.replace(" ", "")
    string = ""
    for i in s:
        index = ABC.index(i)
        newChar = r_ABC[(index + int(shift)) % len(ABC)]
        string += newChar
    msgs.append(string)
print(msgs)
