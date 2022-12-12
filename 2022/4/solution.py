from pathlib import Path
import re

def readFile(filename:str = None) -> str:
    filename = filename or "input.txt"
    filepath = Path(".") / filename
    fileStr = None
    with filepath.open("r") as f:
        fileStr = f.read()
    return fileStr

sectionAssignmentsPairsStr = readFile()

sectionAssignmentsPairs = [[int(section) for section in re.split(",|-", sectionAssignments)] for sectionAssignments in sectionAssignmentsPairsStr.split("\n")]

# print(sectionAssignmentsPairs)

def isContained(start1, end1, start2, end2):
    return (start1 <= start2 and end2 <= end1) or (start2 <= start1 and end1 <= end2)
    # if start1 <= start2 and end1 >= end2:
    #     return True
    # elif start2 <= start1 and end2 >= end1:
    #     return True
    # else:
    #     return False

containings = map(lambda sectionAssignments: isContained(*sectionAssignments), sectionAssignmentsPairs)
print(sum(containings))

def isOverlapping(start1, end1, start2, end2):
    return (start1 <= start2 <= end1) or (start2 <= start1 <= end2)
    # if start1 <= start2 <= end1:
    #     return True
    # elif start2 <= start1 <= end2:
    #     return True
    # else:
    #     return False

overlappings = map(lambda sectionAssignments: isOverlapping(*sectionAssignments), sectionAssignmentsPairs)
print(sum(overlappings))
