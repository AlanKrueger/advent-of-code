import math
import sys

def readNumbers(prefix):
    pieces = sys.stdin.readline().split()
    if prefix != pieces[0]:
        raise ValueError(f'expected "{prefix}" but got "{pieces[0]}"')
    return [int(piece) for piece in pieces[1:]]

def numWins(time, record):
    #print(f'race time={time} record={record}')
    result = 0
    speed = 0
    for t in range(1, time):
        speed = speed + 1
        distance = (time - t) * speed
        #print(f't={t} speed={speed} -> distance={distance}')
        if distance > record:
            #print(f'win')
            result = result + 1
    return result

times = readNumbers("Time:")
distances = readNumbers("Distance:")
if len(times) != len(distances):
    raise ValueError(f'got {len(times)} times but {len(distances)} distances')

numWinsForRaces = [numWins(times[i], distances[i]) for i in range(len(times))]
print(math.prod(numWinsForRaces))