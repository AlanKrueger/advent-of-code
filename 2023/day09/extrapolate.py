import sys

def diffseq(values):
    result = []
    for i in range(1, len(values)):
        result.append(values[i] - values[i - 1])
    return result

def allzeros(values):
    for value in values:
        if value != 0:
            return False
    return True

def extrapolate(values):
    results = []
    stack = []
    stack.append(values)
    while not allzeros(stack[-1]):
        stack.append(diffseq(stack[-1]))
        #print(stack)
    stack[-1].append(0)
    results.append(0)
    while len(stack) > 1:
        values = stack.pop()
        #print(values)
        stack[-1].append(stack[-1][-1] + values[-1])
        results.append(stack[-1][-1])
    return stack[-1][-1]

for line in sys.stdin:
    values = [int(value) for value in line.split()]
    print(extrapolate(values))