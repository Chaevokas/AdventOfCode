from pathlib import Path

filename = "input.txt"
filepath = Path(".") / filename
rucksacksStr: str = None
with filepath.open("r") as file:
    rucksacksStr = file.read()

fullRucksacks = rucksacksStr.split("\n")

scoringList = {chr(ord('a') + i): i + 1 for i in range(26)}
scoringList = {**scoringList, **{chr(ord('A') + i): i + 27 for i in range(26)}}

## solution part 1
rucksackSets = [(set(compartments[:len(compartments)//2]),
                 set(compartments[len(compartments)//2:])) for compartments in fullRucksacks]

intersections = map(lambda compartementSets: compartementSets[0].intersection(
    compartementSets[1]).pop(), rucksackSets)

scoresP1 = map(lambda item: scoringList.get(item), intersections)

print(sum(scoresP1))

## solution part 2
groups = [(set(fullRucksacks[i]), set(fullRucksacks[i+1]), set(fullRucksacks[i+2])) for i in range(0, len(fullRucksacks), 3)]

badges = map(lambda group: group[0].intersection(group[1]).intersection(group[2]).pop(), groups)

scoresP2 = map(lambda badge: scoringList.get(badge), badges)

print(sum(scoresP2))