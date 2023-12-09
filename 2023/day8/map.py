import re
import sys

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

linePattern = re.compile("(\w+) = \((\w+), (\w+)\)")
start = 'AAA'
end = 'ZZZ'

nodes = {}

directions = sys.stdin.readline().strip()
sys.stdin.readline()

for line in sys.stdin:
    match = linePattern.match(line.strip())
    name = match.group(1)
    left = match.group(2)
    right = match.group(3)
    node = Node(name, left, right)
    nodes[node.name] = node

node = nodes[start]
count = 0

while node.name != end:
    for dir in directions:
        if node.name == end:
            break
        match dir:
            case 'L':
                node = nodes[node.left]
            case 'R':
                node = nodes[node.right]
        count = count + 1

print(count)