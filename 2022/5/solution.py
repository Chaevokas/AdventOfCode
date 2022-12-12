from pathlib import Path

part2 = True


def readFile(filename: str = None) -> str:
    filename = filename or "input.txt"
    filepath = Path(".") / filename
    fileStr = None
    with filepath.open("r") as f:
        fileStr = f.read()
    return fileStr


positionRowsStr = readFile("inputPosition.txt")
movesStr = readFile("inputMoves.txt")


def extractStartingPositionsAsRows(positionRowStr: str):
    return [positionRowStr[i+1] for i in range(0, len(positionRowStr), 4)]


positionRows = map(extractStartingPositionsAsRows,
                   positionRowsStr.split("\n")[:-1][::-1])  # cut off last row, and reverse roworder
# print(list(positionsRows))

positions = [[item for item in column if item != " "]
             for column in zip(*positionRows)]  # transpose and remove empty boxes
# print(positions)


def extractMoves(moveStr: str):
    (_, number, _, fromStack, _, toStack) = moveStr.split(" ")
    return (int(number), int(fromStack)-1, int(toStack)-1)


moves = map(extractMoves, movesStr.split("\n"))


if not part2:
    # solution for part 1
    for move in moves:
        for _ in range(move[0]):
            positions[move[2]].append(positions[move[1]].pop())
else:
    # solution for part 2
    for move in moves:
        positions[move[2]].extend(positions[move[1]][-move[0]:])
        positions[move[1]] = positions[move[1]][:-move[0]]
# print(positions)

print("".join(map(lambda l: l[-1], positions)))
