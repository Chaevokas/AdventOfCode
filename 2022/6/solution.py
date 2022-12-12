from pathlib import Path

def readFile(filename:str = None) -> str:
    filename = filename or "input.txt"
    filepath = Path(".") / filename
    fileStr = None
    with filepath.open("r") as f:
        fileStr = f.read()
    return fileStr

part1 = False

datastream = readFile()
maxPosition = len(datastream)

# solution Part 1
if part1:
    sopFound = False
    position = 4

    while not sopFound:
        chars = set(datastream[position - 4:position])
        if len(chars) == 4:
            print(position)
            sopFound = True
            
        position += 1
        if position > maxPosition:
            print("nothing found")
            sopFound = True
else:
    somFound = False
    position = 14

    while not somFound:
        chars = set(datastream[position - 14:position])
        if len(chars) == 14:
            print(position)
            somFound = True

        position += 1
        if position > maxPosition:
            print("nothing found")
            somFound = True
