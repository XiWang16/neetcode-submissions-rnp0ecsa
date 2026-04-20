class MinStack:

    def __init__(self):
        self.min = None
        self.items = []
        self.items_sorted = []

    def push(self, val: int) -> None:
        if self.min == None:
            self.min = val
        if val < self.min:
            self.min = val
        self.items.append(val)
        self.items_sorted.append(val)
        self.items_sorted.sort()

    def pop(self) -> None:
        
        self.items_sorted.remove(self.items.pop())
        self.min = self.items_sorted[0] if len(self.items_sorted) > 0 else None

    def top(self) -> int:
        if self.items != []:
            return self.items[-1]
        

    def getMin(self) -> int:
        return self.min
        
