class Heap:
    arr: list[int]

    def __init__(self):
        self.arr = []

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        return (i * 2) + 1

    def right_child(self, i: int) -> int:
        return (i * 2) + 2

    def shift_up(self, i: int):
        parent = self.parent(i)
        while i > 0 and self.arr[parent] < self.arr[i]:
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            parent = self.parent(i)

    def shift_down(self, i: int):
        while True:
            left_child = self.left_child(i)
            right_child = self.right_child(i)
            if left_child < len(self.arr) and self.arr[left_child] > self.arr[i]:
                self.arr[left_child], self.arr[i] = self.arr[i], self.arr[left_child]
                i = left_child
            elif right_child < len(self.arr) and self.arr[right_child] > self.arr[i]:
                self.arr[right_child], self.arr[i] = self.arr[i], self.arr[right_child]
                i = right_child
            else:
                break

    def insert(self, i: int):
        self.arr.append(i)
        self.shift_up(len(self.arr) - 1)

    def extract_max(self) -> int:
        result = self.arr[0]
        leaf = self.arr.pop()
        if self.arr:
            self.arr[0] = leaf
            self.shift_down(0)
        return result


h = Heap()
h.insert(3)
h.insert(10)
h.insert(5)
h.insert(20)
h.extract_max()
h.extract_max()
h.extract_max()
h.extract_max()
