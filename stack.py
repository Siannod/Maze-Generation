class Stack:
  def __init__(self, maxSize):
    self.stack = ["#"] * maxSize #generates array for stack
    self.top = -1
    self.maxSize = maxSize

  def isFull(self): #checks if stack is full
    if self.top == self.maxSize:
      return True
    else:
      return False

  def isEmpty(self):#checks if stack is empty
      if self.top == -1:
        return True
      else:
        return False
  def push(self, item): #adds item to stack
    if self.isFull():
      print("Stack is full")
    else:
      self.top += 1
      self.stack[self.top] = item

  def pop(self): #removes top item from stack
    if self.isEmpty():
      print("Stack is empty")
    else:
      self.temp = self.stack[self.top]

      self.top -= 1
      return self.temp

  def reverse_stack(self): #reverse stack to have bottom at the top
    tempQ = []
    while self.isEmpty() == False:
        tempQ.append(self.pop())
    while len(tempQ) != 0:
        self.push(tempQ.pop(0))

  def empty(self): #empties the stack
    for i in range(len(self.stack)):
        if self.stack[i] == ["#"]:
            pass
        else:
            self.stack[i] = ["#"]
    self.top = -1