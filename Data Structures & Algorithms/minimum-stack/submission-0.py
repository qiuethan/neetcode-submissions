class MinStack:

    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._min) > 0:
            self._min.append(min(self._min[-1], val))
        else:
            self._min.append(val)

    def pop(self) -> None:
        val = self._stack.pop(-1);
        self._min.pop(-1);
        return val

    def top(self) -> int:
        val = self._stack[-1]
        return val

    def getMin(self) -> int:
        return self._min[-1]
