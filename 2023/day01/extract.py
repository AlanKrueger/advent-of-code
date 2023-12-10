import sys
import re

digitWords = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

pattern = re.compile("|".join(digitWords.keys()))

def replaceWords(line):
    result = ""
    match = re.search(pattern, line)
    while match != None:
        word = line[match.start():match.end()]
        line = line[match.start()+1:]
        result = result + digitWords[word]
        match = re.search(pattern, line)
    return result

def extractDigits(line):
    chars = []
    chars.extend(line)
    #print(chars)

    digits = [ch for ch in chars if ch.isdigit()]
    #print(digits)

    cal = []
    cal.append(digits[0])
    cal.append(digits[-1])
    #print(cal)

    return int("".join(cal))


for line in sys.stdin:
    line = line.strip()
    print(extractDigits(replaceWords(line)))
