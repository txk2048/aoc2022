from typing import Optional


class Node:
    def __init__(
        self,
        name: str,
        is_dir: bool,
        parent: Optional["Node"] = None,
        size: int | None = None,
    ) -> None:
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self._size = size

        self._children: Optional[list[Node]] = None
        if self.is_dir:
            self._children = []

    def get_size(self) -> int:
        if self.is_dir:
            # return cached size
            if self._size is not None:
                return self._size

            self._size = sum(child.get_size() for child in self._children)
            return self._size
        else:
            return self._size

    def get_child(self, name: str) -> Optional["Node"]:
        for child in self._children:
            if child.name == name:
                return child

        return None

    def add_child(self, child: "Node") -> None:
        assert self.is_dir  # this method should only be called on directories
        self._children.append(child)
        self._size = None


nodes = []
root = Node(name="/", is_dir=True, parent=None, size=None)
curr = None
with open("input.txt") as f:
    lines = f.readlines()

index = 0
while index < len(lines):

    if not lines[index].startswith("$"):
        raise ValueError("Invalid input, command not specified")

    # command
    command = lines[index].split()[1:]

    if command[0] == "cd":
        target = command[1]

        if target == "/":
            curr = root
        elif target == "..":
            curr = curr.parent
        else:
            curr = curr.get_child(target)

        index += 1
        continue

    elif command[0] == "ls":
        index += 1  # move forward one line to the listing
        while index < len(lines) and not lines[index].startswith("$"):
            size, name = lines[index].split()
            if size == "dir":
                child = Node(name, is_dir=True, parent=curr)
                curr.add_child(child)

                nodes.append(child)
            else:
                child = Node(name, is_dir=False, parent=curr, size=int(size))
                curr.add_child(child)

                nodes.append(child)

            index += 1

    else:
        raise ValueError("Unrecognised command")

directories = sorted(
    [node for node in nodes if node.is_dir], key=lambda dir_: dir_.get_size()
)
result = 0
for dir_ in directories:
    size = dir_.get_size()
    if size > 100000:
        break

    result += size

print(f"Part 1: {result}")

free_space = 70000000 - root.get_size()
for dir_ in directories:
    if free_space + dir_.get_size() >= 30000000:
        # this is the directory we want
        print(f"Part 2: {dir_.get_size()}")
        break
