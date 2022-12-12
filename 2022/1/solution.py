from pathlib import Path

filename = "input.txt"
filepath = Path(".") / filename
elfListStr = None
with filepath.open("r") as file:
    elfListStr = file.read()

sacks = [[int(item) for item in sackStr.split("\n")] for sackStr in elfListStr.split("\n\n")]

elfTotalColories = [sum(sack) for sack in sacks]

# print(max(elfTotalColories))

elfTotalColories.sort(reverse=True)
top3 = elfTotalColories[:3]
print(sum(top3))