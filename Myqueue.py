class MyQueue:
    def __init__(self,maxSize):
        self.Maxsize = maxSize
        self.queue = [[1000000]]*maxSize #generate array for queue
        self.end = 0

    def add(self, item):
        if self.end == 0:
            self.queue[self.end] = item
            self.end += 1
        elif self.isFull(): #checks if its full
            for i in range(self.end + 1):
                if self.queue[i][0] == item[0]:
                    pass
                elif self.queue[i][0] > item[0]:
                    if self.queue[i][0] == 1000000:
                        self.queue[i] = item
                        self.end += 1
                        break
                    else:
                        for j in range(self.end-1, i-1, -1):
                            self.temp = self.queue[j]
                            self.queue[j+1] = self.temp
                        self.queue[i] = item
                        self.end += 1
                        break
        else:
            pass

    def remove(self): #removes and returns first item in queue
        if self.isEmpty():
            self.temp = self.queue[0]
            self.queue.pop(0)
            self.queue.append([1000000])
            self.end -= 1
            return self.temp
        else:
            pass

    def isFull(self): # checks if queue is full
        if self.end == self.Maxsize:
            return False
        else:
            return True

    def isEmpty(self): #checks if queue is empty
        if self.end == 0:
            return False
        else:
            return True