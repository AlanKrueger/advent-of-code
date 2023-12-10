import re
import sys

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.name}: ({self.left}, {self.right})'
    
    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def parseFrom(line):
        match = linePattern.match(line.strip())
        name = match.group(1)
        left = match.group(2)
        right = match.group(3)
        return Node(name, left, right)


linePattern = re.compile("(\w+) = \((\w+), (\w+)\)")

nodes = {}

directions = sys.stdin.readline().strip()
sys.stdin.readline()

rawNodes = [Node.parseFrom(line) for line in sys.stdin]
nodes = {node.name: node for node in rawNodes}

def atEnd():
    for node in curNodes:
        if node.name[-1] != 'Z':
            return False
    return True

def navigate(node, dir):
    match dir:
        case 'L':
            return nodes[node.left]
        case 'R':
            return nodes[node.right]

curNodes = [node for node in nodes.values() if node.name[-1] == 'A']
count = 0

#print(f'starting at {curNodes}')
while not atEnd():
    for dir in directions:
        old = curNodes
        if atEnd():
            break
        curNodes = [navigate(node, dir) for node in curNodes]
        count = count + 1
        #print(f'{dir}: {old} -> {curNodes} ({count})')

print(count)