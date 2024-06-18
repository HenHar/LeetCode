class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        return None

    def pop(self) -> int:
        if self.empty():
           return 0

        queue_temp = []
        while len(self.queue) > 1:
            queue_temp.append(self.queue.pop(0))

        first = self.queue.pop(0)
        self.queue = queue_temp
        return first

    def top(self) -> int:
        if self.empty():
            return 0

        queue_temp = []
        while len(self.queue) > 1:
            queue_temp.append(self.queue.pop(0))

        first = self.queue.pop(0)
        queue_temp.append(first)
        self.queue = queue_temp
        return first
            
    def empty(self) -> bool:
        return len(self.queue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()