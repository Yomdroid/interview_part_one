"""Implement a class for a stack that supports all the regular functions (push, pop) and an additional function
of max() which returns the maximum element in the stack (return None if the stack is empty). Each method
should run in constant time."""

class MaxStack:
  def __init__(self):
    self.stack = []
  def push(self, new):
    self.stack.append(new)
  def pop(self):
    self.stack.pop()
  def max(self):
    x = 0
    for item in self.stack:
      if len(self.stack) == 0:
        return None
      if item > x:
        x = max(item, x)
    return x

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
s.pop()
s.pop()
print(s.max())
