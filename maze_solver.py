from stack import *
import time
from Myqueue import *

class Solver:

    def __init__(self, screen):
        
        self.window = screen
        self.stack = Stack(100000)
        self.x = 1
        self.y = 1

        self.i = 4
        self.sleep = 0.01
        self.movements = [ 
            (-1, 0),  # Up
            (1, 0),  # Down
            (0, -1),  # Left
            (0, 1)  # Right
        ] #the moves in X y Y differences 
        
    def range(self, x, y, move): #checks if move is in range
        if x + move[0] < 0 or x + move[0] >= len(self.Maze) or y + move[1] < 0 or y + move[1] >= len(self.Maze):  # range
            return True
        elif self.Maze[x+move[0]][y+move[1]] == 1:
            return True
                   
    
    def solver(self, maze):
        self.Maze = maze
        self.running = True
        self.stack.empty()
        self.x = 1
        self.y = 1
        self.i = 3
        self.visited = [[self.x, self.y]]
        while self.running:
            time.sleep(self.sleep)
            self.window.draw_solver(self.x, self.y) #draw solvers position
            if self.Maze[self.x][self.y] == 3: #checks if solver at the end
                break
            else:
                if self.i == -1:  # tested all directions
                    self.stack.pop() #pop off top of stack
                    self.window.clear_solver(self.x, self.y) #clear solvers position
                    self.x = self.stack.temp[0][0]
                    self.y = self.stack.temp[0][1]
                    self.i = self.stack.temp[1][0]
                    self.window.draw_solver(self.x, self.y)
                else:
                    self.move = self.movements[self.i]
                    if self.range(self.x, self.y, self.movements[self.i]):
                        self.i -= 1
                        pass
                    elif [self.x + self.move[0], self.y + self.move[1]] in self.visited:
                        self.i -= 1
                        pass
                    else:  # move forward
                        self.i -= 1
                        self.stack.push([[self.x, self.y], [self.i]]) #adds current position to stack
                        self.visited.append([self.x, self.y]) #add to visited
                        self.x += self.move[0] #sets new x, y
                        self.y += self.move[1]
                        self.window.draw_solver(self.x, self.y)
                        self.i = 3

    def breadth_first(self, maze):
        self.Maze = maze
        self.running = True
        self.queue = MyQueue(100000)
        self.x = 1
        self.y = 1
        self.queue.add([self.x, self.y]) #adds start to queue
        self.visited = []
        while self.running:
            time.sleep(self.sleep+0.01)
            if self.Maze[self.x][self.y] == 3: #end of maze
                break
            else:
                self.queue.remove() #removes next in queue
                self.x = self.queue.temp[0] #sets x y to next spot
                self.y = self.queue.temp[1]
                self.window.draw_solver(self.x, self.y)
                for i in range(len(self.movements)):
                    if [self.x + self.movements[i][0], self.y + self.movements[i][1]] in self.visited: #checks if its been visited
                        pass
                    elif self.range(self.x, self.y, self.movements[i]):
                        self.visited.append([self.x + self.movements[i][0], self.y + self.movements[i][1]]) #adds to visited list
                        pass
                    else:
                        self.visited.append([self.x + self.movements[i][0], self.y + self.movements[i][1]])
                        self.queue.add([self.x + self.movements[i][0], self.y + self.movements[i][1]]) #adds to queu to visit

    def a_star(self, maze):
        self.Maze = maze
        self.running = True
        self.endX = 49
        self.endY = 49
        self.x = 1
        self.y = 1
        self.steps = 0
        self.queue = MyQueue(1000)
        self.visited = []
        self.queue.add([self.steps + (self.endX - self.x) + (self.endY - self.y), self.x, self.y])
        while self.running:
            time.sleep(self.sleep)
            self.window.draw_solver(self.x, self.y)
            if self.Maze[self.x][self.y] == 3:
                break
            else:
                self.queue.remove()
                self.x = self.queue.temp[1]
                self.y = self.queue.temp[2]
                for i in range(len(self.movements)):
                    if [self.x + self.movements[i][0], self.y + self.movements[i][1]] in self.visited:
                        pass
                    elif self.range(self.x, self.y, self.movements[i]):
                        self.visited.append([self.x + self.movements[i][0], self.y + self.movements[i][1]]) #adds to visited
                        pass
                    else:
                        self.visited.append([self.x + self.movements[i][0], self.y + self.movements[i][1]])
                        self.queue.add([int(self.steps + (self.endX - self.x) + (self.endY - self.y)),
                                        self.x + self.movements[i][0], self.y + self.movements[i][1]])
