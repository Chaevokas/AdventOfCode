from pathlib import Path
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from functools import reduce


def readFile(filename: str = None):
    filename = filename or "input.txt"
    filepath = Path(filename)
    file = None
    with filepath.open("r") as fp:
        file = fp.read()
    return file


part1 = False

gridStr = readFile()
grid = np.array([[np.uint8(treehight) for treehight in line]
                for line in gridStr.split("\n")])


# Part 1
# doing this via dynamic programming

# left, up, right, down
highestVisibleTreesList = np.zeros((4, *grid.shape), dtype=np.uint8)
visiblesList = np.zeros_like(highestVisibleTreesList, dtype=bool)

highestVisibleTreesList[0, :, 0] = grid[:, 0]
highestVisibleTreesList[1, 0, :] = grid[0, :]
highestVisibleTreesList[2, :, -1] = grid[:, -1]
highestVisibleTreesList[3, -1, :] = grid[-1, :]

visiblesList[0, :, 0] = True
visiblesList[1, 0, :] = True
visiblesList[2, :,-1] = True
visiblesList[3,-1, :] = True



def setHighestVisibleTrees(slice):
    # slice should be just 1 whole row/column

    # for grid: do not use first dimension (that is the direction)
    # start at element at index 1, not zero
    for index in range(1, len(grid[slice[1:]])):
        treeHight = grid[slice[1:]][index]
        treeHightInFront = highestVisibleTreesList[slice][index-1]

        highestVisibleTreesList[slice][index] = np.maximum(treeHight, treeHightInFront)
        visiblesList[slice][index] = treeHight > treeHightInFront


# left to right
def getSlices(direction, shape):
    if direction == "left" or direction == 0:
        return (np.index_exp[0, i, :] for i in range(shape[0]))

    if direction == "up" or direction == 1:
        return (np.index_exp[1, :, i] for i in range(shape[1]))

    if direction == "right" or direction == 2:
        return (np.index_exp[2, i, ::-1] for i in range(shape[0]))

    if direction == "down" or direction == 3:
        return (np.index_exp[3, ::-1, i] for i in range(shape[1]))

# with ThreadPoolExecutor(max_workers=4) as tpe:
#     for _ in tpe.map(lambda direction: map(setHighestVisibleTrees, getSlices(direction, grid.shape)), range(4)):
#         pass
for direction in range(4):
    for slice in getSlices(direction, grid.shape):
        setHighestVisibleTrees(slice)

visibleFromAnySide = reduce(np.logical_or, visiblesList[:])
# print(np.sum(visibleFromAnySide))

# Part 2
# can probably also be done via dynamic programming, however this seems complexer to me than necessary

def getVisibleLength(slice, maxTreeHeight):
    index = 0
    # print(grid[slice])
    for (index, treeHeight) in enumerate(grid[slice], start=1):
        if treeHeight >= maxTreeHeight:
            break
    return index

scenicScores = np.empty_like(grid, dtype=np.uint32)
for (index, treeHeight) in np.ndenumerate(grid):    
    visibleLeft  = getVisibleLength(np.index_exp[index[0], range(index[1]-1, -1, -1)], treeHeight)
    visibleAbove = getVisibleLength(np.index_exp[range(index[0]-1, -1, -1), index[1]], treeHeight)
    visibleRight = getVisibleLength(np.index_exp[index[0], index[1]+1:], treeHeight)
    visibleBelow = getVisibleLength(np.index_exp[index[0]+1:, index[1]], treeHeight)

    scenicScores[index] = visibleLeft*visibleAbove*visibleRight*visibleBelow
    
print(scenicScores.max())