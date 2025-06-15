class HashTableNode[T]:
    key: int
    value: T
    offset: int

    def __init__(self, key: int, value: T):
        self.key = key
        self.value = value
        self.offset = 0


class HashTable[T]:
    size: int
    table: list[HashTableNode[T] | None]

    def __init__(self, size: int):
        self.size = size
        self.table = [None] * size

    def insert(self, key: int, value: T):
        pos = abs(key % self.size)
        curr = HashTableNode(key, value)
        while found := self.table[pos]:
            if curr.offset == found.offset and curr.key == found.key:
                found.value = curr.value
                return
            elif curr.offset > found.offset:
                self.table[pos], curr = curr, found

            pos = (pos + 1) % self.size
            curr.offset += 1
        self.table[pos] = curr

    def get(self, key: int) -> T | None:
        pos = abs(key % self.size)
        offset = 0
        while found := self.table[pos]:
            if offset > found.offset:
                return None
            elif offset == found.offset and key == found.key:
                return found.value

            pos = (pos + 1) % self.size
            offset += 1
        return None

    def remove(self, key: int):
        pos = abs(key % self.size)
        offset = 0
        while found := self.table[pos]:
            if offset > found.offset:
                return
            elif offset == found.offset and key == found.key:
                self.table[pos] = None
                # Backwards shift
                next_pos = (pos + 1) % self.size
                while (next_found := self.table[next_pos]) and next_found.offset != 0:
                    next_found.offset -= 1
                    self.table[pos], self.table[next_pos] = (
                        self.table[next_pos],
                        self.table[pos],
                    )
                    pos = (pos + 1) % self.size
                    next_pos = (next_pos + 1) % self.size
                return

            pos = (pos + 1) % self.size
            offset += 1


table: HashTable[str] = HashTable(5)
table.insert(3, "hello")
table.insert(13, "world")
table.get(3)
table.get(13)
table.remove(3)
table.get(13)
table.insert(3, "blah")
table.get(13)
table.get(3)
