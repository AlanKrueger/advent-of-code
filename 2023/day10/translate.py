import sys

src='|-LJ7F.'
dst='│─└┘┐┌·'

for line in sys.stdin:
    for i in range(len(src)):
        line = line.replace(src[i], dst[i])
    print(line, end="")