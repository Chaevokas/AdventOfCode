from pathlib import Path
import re
import operator

def readFile(filename:str = None):
    filename = filename or "input.txt"
    filepath = Path(filename)
    file = None
    with filepath.open("r") as fp:
        file = fp.read()
    return file

part1 = False

commandsStr = readFile()
commands = commandsStr.split("\n")

# construct directory structure

class Node:
    def __init__(self, name:str, size:int = 0, parent = None, childeren:dict = None, isDirectory:bool = False, depth = 0):
        self.name = name
        self.size = size
        self.parent = parent
        self.childeren = childeren or {}
        self.isDirectory = isDirectory
        self.depth = depth
    
    def addChild(self, childNode):
        self.childeren[childNode.name] = childNode
        childNode.parent = self
        childNode.depth = self.depth + 1
    
    def getChild(self, childName):
        return self.childeren.get(childName, None)

    def getParent(self):
        return self.parent
    
    def __str__(self) -> str:
        s = ""
        if self.isDirectory:
            s += "\t"*self.depth + f"{self.name} (dir, size={self.size})"
            for child in self.childeren.values():
                s += f"\n{str(child)}"
        else:
            s = "\t"*self.depth + f"{self.name} (file, size={self.size})"
        return s

    def getSize(self) -> int:
        if self.isDirectory and self.size == 0:
            self.size = sum([child.getSize() for child in self.childeren.values()])
        return self.size

rootNode = Node("/", isDirectory=True)
currentNode = rootNode 

cdPattern = re.compile(r"\$ cd (?P<to>.+)")
# lsPattern = re.compile(r"\$ ls")
dirPattern = re.compile(r"dir (?P<name>\w+)")
filePattern = re.compile(r"(?P<size>\d+) (?P<name>.+)")

for command in commands[1:]: # skip first commmand, this one is done by "rootNode = Node("/", isDirectory=True)"
    cd = cdPattern.fullmatch(command)
    # ls = lsPattern.fullmatch(command)
    dir = dirPattern.fullmatch(command)
    file = filePattern.fullmatch(command)

    if cd:
        to = cd.group("to")
        if to == "..":
            currentNode = currentNode.getParent()
        else:
            currentNode = currentNode.getChild(to)
    elif dir or file:
        if dir:
            currentNode.addChild(Node(dir.group("name"), isDirectory=True))
        else:
            currentNode.addChild(Node(file.group("name"), size = int(file.group("size"))))
    else:
        pass # is an ls command

def getdirs(node:Node, cutoff:int, op) -> list[Node]:
    dirs:list[Node] = []
    if node.isDirectory:
        size = node.getSize()
        if op(size, cutoff):
            dirs.append(node)
        for child in node.childeren.values():
            dirs.extend(getdirs(child, cutoff, op))
    return dirs



if part1:
    # part 1
    dirs = getdirs(rootNode, 100000, operator.lt)
    print(sum(dir.getSize() for dir in dirs))
    
else:
    # part 2
    totalSize = 70000000
    currentFree = totalSize - rootNode.getSize()
    minFree = 30000000
    toFree = minFree - currentFree
    if toFree > 0:
        dirs = getdirs(rootNode, toFree, operator.gt)
        print(min(dir.getSize() for dir in dirs))
    else:
        print("already enough free space")
    