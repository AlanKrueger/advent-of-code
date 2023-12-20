# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, non-ascii-name, too-few-public-methods

from __future__ import annotations
import sys

def HASH(string):
    value = 0
    for ch in string:
        value += ord(ch)
        value *= 17
        value %= 256
    return value

boxes = [[] for _ in range(256)]
for line in sys.stdin:
    for part in line.strip().split(','):
        if "=" in part:
            label, focalLength = part.split('=', 2)
            lenses = boxes[HASH(label)]
            found = None
            for i, pair in enumerate(lenses):
                if pair[0] == label:
                    found = i
                    break
            newpair = tuple([label, int(focalLength)])
            if found is not None:
                lenses[found] = newpair
            else:
                lenses.append(newpair)
        if "-" in part:
            label = part.split('-', 1)[0]
            lenses = boxes[HASH(label)]
            found = None
            for i, pair in enumerate(lenses):
                if pair[0] == label:
                    found = i
                    break
            if found is not None:
                del lenses[found]

        #print(f'After "{part}":')
        #for i, lenses in enumerate(boxes):
        #    if len(lenses) > 0:
        #        print(f'Box {i}: {" ".join([f"[{pair[0]} {pair[1]}]" for pair in lenses])}')
        #print()

for i, lenses in enumerate(boxes):
    for j, pair in enumerate(lenses):
        #print(f'{pair[0]}: {i + 1} (box {i}) * {j + 1} (slot {j}) * {pair[1]} (focal length) =')
        print((i + 1) * (j + 1) * pair[1])
