import random
from stack import *

class Generator:
    def __init__(self, size, screen):
        self.size = 50 #sets size for maze
        self.Maze = [[1]*self.size for i in range(self.size)] #generates array for maze
        self.stack = Stack(1000)
        self.directions = {1: [[-2, 0], [-1, 0]],
                           2: [[0, 2], [0, 1]],
                           3: [[2, 0], [1, 0]],
                           4: [[0, -2], [0, -1]]} #list of directions it can move
        
    
    def range(self, x, y, move): #checks if move is in range
        if x + move[0][0] < 0 or y + move[0][1] < 0:
            return True
        elif x + move[0][0] > len(self.Maze[x])-1 or y + self.move[0][1] > len(self.Maze)-1:
            return True
        else:
            return False

    def depth_first_gen(self):
        self.passes = 0
        self.x = 1
        self.y = 1
        self.tested = []
        self.running = True
        while self.running:
            self.direction = random.randint(1, 4)
            if self.direction in self.tested:
                if len(self.tested) == 4:
                  self.stack.pop()
                  self.x = self.stack.temp[0][0]
                  self.y = self.stack.temp[0][1]
                  self.tested = self.stack.temp[1]
                else:
                  pass #if it has already been tested
            else: #NOT BEEN TESTED
                self.move = self.directions[self.direction] #takes the random number and finds the direction it wants to move in
                if self.range(self.x, self.y, self.move):
                    self.tested.append(self.direction)
                else:   #NOT OUT OF RANGE  NOT BEEN TESTED
                    if self.Maze[self.x + self.move[0][0]][self.y + self.move[0][1]] == 0: #tests if its already a path
                        self.tested.append(self.direction)
                        pass
                    else:   #NOT OUT OF RANGE   NOT BEEN TESTED     NOT ALREADY A PATH
                        self.Maze[self.x + self.move[0][0]][self.y + self.move[0][1]] = 0
                        self.Maze[self.x + self.move[1][0]][self.y + self.move[1][1]] = 0
                        self.tested.append(self.direction)
                        self.stack.push([[self.x, self.y], self.tested])
                        self.x += self.move[0][0]
                        self.y += self.move[0][1]
                        self.passes += 1
                        self.tested = []
            if self.stack.top == -1 and self.passes > 1:
                self.Maze[1][1] = 2
                self.Maze[-1][-1] = 3
                break
            else:
              pass

    def prims(self):
        self.wallx = 1
        self.wally = 1
        self.walls = [[3, 1, 3], [1, 3, 2]]
        self.visited = []
        self.running = True
        self.Maze[1][1] = 0
        while self.running:
            if len(self.walls) == 0:
                break
            else: #make new path
                self.new = random.randint(0, len(self.walls)-1) #randomly selectsd new path from list
                self.wallx = self.walls[self.new][0]
                self.wally = self.walls[self.new][1]
                self.back = self.walls[self.new][2]
                if self.Maze[self.wallx][self.wally] == 0: #already a path
                    pass
                else:
                    self.Maze[self.wallx][self.wally] = 0 #makes it a path
                    self.Maze[self.wallx - self.directions[self.back][1][0]][self.wally - self.directions[self.back][1][1]] = 0 #connects path up
                self.visited.append([self.wallx, self.wally, self.back]) #adds new path to visited
                self.walls.pop(self.new) #removes path from list of walls
                self.path_count = 0
                for key in self.directions: #checks surroundings of newe path
                    self.tempx = self.wallx + self.directions[key][0][0]
                    self.tempy = self.wally + self.directions[key][0][1]
                    if 0 < self.tempx < len(self.Maze)  and 0<self.tempy<len(self.Maze) and self.Maze[self.tempx][self.tempy] == 1: #checks if co-ord is path and in maze
                        if [self.tempx, self.tempy, key] in self.visited: #checks if its already visited
                            pass
                        else:
                            self.walls.append([self.tempx, self.tempy, key]) #add to list of walls
                    else:
                        pass
        self.Maze[-1][-1] = 3 #assigns start and finish
        self.Maze[1][1] = 2