from pathlib import Path

filename = "input.txt"
filepath = Path(".") / filename
resultsStr = None
with filepath.open("r") as file:
    resultsStr = file.read()

results = [tuple(result.split(" ")) for result in resultsStr.split("\n")]

scoringList = {}
## scoringlist for part 1
# scoringList[('A', 'X')] = 1 + 3
# scoringList[('A', 'Y')] = 2 + 6
# scoringList[('A', 'Z')] = 3 + 0
# scoringList[('B', 'X')] = 1 + 0
# scoringList[('B', 'Y')] = 2 + 3
# scoringList[('B', 'Z')] = 3 + 6
# scoringList[('C', 'X')] = 1 + 6
# scoringList[('C', 'Y')] = 2 + 0
# scoringList[('C', 'Z')] = 3 + 3

## scoringlist for part 2
scoringList[('A', 'X')] = 3 + 0
scoringList[('B', 'X')] = 1 + 0
scoringList[('C', 'X')] = 2 + 0
scoringList[('A', 'Y')] = 1 + 3
scoringList[('B', 'Y')] = 2 + 3
scoringList[('C', 'Y')] = 3 + 3
scoringList[('A', 'Z')] = 2 + 6
scoringList[('B', 'Z')] = 3 + 6
scoringList[('C', 'Z')] = 1 + 6

scores = map(lambda x: scoringList.get(x), results)

totalscore = sum(scores)
print(totalscore)