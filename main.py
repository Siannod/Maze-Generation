from database import *
from window import *
from maze_gen import *
from maze_solver import *
import pygame
import sys
import time


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((510, 510)) #creates a window for pygame
        pygame.display.set_caption("Maze") #sets window name
        self.win = Window(self.screen) #creates class for window
        self.solver = Solver(self.win) #creates class for solver
        self.db = Database()
        self.user = ""

    def close(self): #code for closing the program
        self.db.close()
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def point_check(self, mouse, point, mod = 0):
        if (70 + (50*point)) <= mouse[1] <= (70 + (50*point)+mod) and 40 <= mouse[0] <= 470: #checks location of cursor
            return True
        else:
            return False

    def login_signup(self):
        self.win.fill()
        self.win.draw_login_signup() #calls code to draw login signup screen
        self.login_signup_buttons = True
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.point_check(self.mouse, 1, 70):
                        self.login()
                        pass
                        # login
                    if self.point_check(self.mouse, 3, 70):
                        self.signup()
                        pass
                        # signup

    def login(self):
        self.login_buttons = True
        self.username = ""
        self.password = ""
        self.Useractive = False
        self.win.fill()
        self.Passactive = False
        while self.running:
            self.win.draw_login(self.username, self.password) #calls code to draw the login page
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN: #checks if user is clicking mouse
                    self.mouse = pygame.mouse.get_pos()  # gets postion of the mouse
                    if 40 <= self.mouse[0] <= 470 and self.win.point_one + 20 <= self.mouse[
                        1] <= self.win.point_one + 50 and self.login_buttons: #clicks on the username box
                        self.Useractive = True
                        self.Passactive = False
                    elif 40 <= self.mouse[0] <= 470 and self.win.point_three + 20 <= self.mouse[
                        1] <= self.win.point_three + 50 and self.login_buttons: #clicks on the password box
                        self.Passactive = True
                        self.Useractive = False
                    elif 205 <= self.mouse[0] <= 305 and self.win.point_four + 20 <= self.mouse[
                        1] <= self.win.point_four + 80 and self.login_buttons:
                        if self.db.check_login(self.username, self.password): #checks if username and password match entry
                            self.login_signup_buttons = False
                            self.user = self.username
                            self.menu() #moves onto main menu
                        else:
                            self.username = ""
                            self.password = ""
                            self.win.failed_login() #gives error message, no match
                    elif 100 <= self.mouse[0] <= 305 and self.win.point_six <= self.mouse[
                        1] <= self.win.point_six + 40 and self.login_buttons: #back button
                        self.login_signup()
                if event.type == pygame.KEYDOWN and self.Useractive or event.type == pygame.KEYDOWN and self.Passactive: #checks if user is typing
                    if event.key == pygame.K_BACKSPACE and self.Useractive: #checks if user is pressing backspace
                        self.username = self.username[:-1] #removes last letter from relevant string
                    elif event.key == pygame.K_BACKSPACE and self.Passactive:
                        self.password = self.password[:-1]
                    elif event.key == pygame.K_RETURN and self.Useractive:
                        self.Passactive = True
                        self.Useractive = False
                    elif event.key == pygame.K_RETURN and self.Passactive:
                        if self.db.check_login(self.username, self.password):
                            self.login_buttons = False
                            self.user = self.username
                            self.menu()
                    else:
                        if self.Useractive:
                            self.username += event.unicode #adds users typing to username
                        elif self.Passactive:
                            self.password += event.unicode

    def signup(self):
        self.signup_buttons = True
        self.username = ""
        self.passwordOne = ""
        self.passwordTwo = ""
        self.Useractive = False
        self.PassOneActive = False
        self.PassTwoActive = False
        self.running = True
        self.userFree = False
        self.passMatch = False
        self.win.fill()
        while self.running:
            self.win.draw_signup(self.username, self.passwordOne, self.passwordTwo) #draws signup page to screen
            if self.db.check_user(self.username): #checks if username is already in use
                self.win.user_taken() #displays user taken
            else:
                self.win.box(0, self.win.point_one + 50, 510, 30) #covers error message
                if len(self.username) > 0:
                    self.userFree = True
            if self.passwordOne != self.passwordTwo: #checks if passwords match
                self.win.pass_error()
            else:
                self.win.box(0, self.win.point_four + 30, 510, 30) #covers error message
                if len(self.passwordOne) > 1:
                    self.passMatch = True
            for event in pygame.event.get():
                self.mouse = pygame.mouse.get_pos() #checks mouse position
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN: #checks for mouse click
                    if 40 <= self.mouse[0] <= 470 and self.win.point_one + 20 <= self.mouse[
                        1] <= self.win.point_one + 50 and self.signup_buttons:
                        self.Useractive = True
                        self.PassOneActive = False
                        self.PassTwoActive = False
                    elif 40 <= self.mouse[0] <= 470 and self.win.point_three <= self.mouse[
                        1] <= self.win.point_three + 30 and self.signup_buttons:
                        self.PassOneActive = True
                        self.PassTwoActive = False
                        self.Useractive = False

                    elif 40 <= self.mouse[0] <= 470 and self.win.point_four <= self.mouse[
                        1] <= self.win.point_four + 30 and self.signup_buttons:
                        self.PassTwoActive = True
                        self.Useractive = False
                        self.PassOneActive = False

                    elif 205 <= self.mouse[0] <= 305 and self.win.point_five + 20 <= self.mouse[
                        1] <= self.win.point_five + 80 and self.signup_buttons:
                        if self.userFree and self.passMatch:
                            self.db.new_user(self.username, self.passwordOne)
                            self.user = self.username
                            self.menu()
                        else:
                            self.win.draw_text(510 / 2, self.win.point_five + 50,
                                               "USERNAME OR PASSWORD DO NOT MEET REQUIREMENTS")
                    elif 100 <= self.mouse[0] <= 305 and self.win.point_seven <= self.mouse[
                        1] <= self.win.point_seven + 40 and self.signup_buttons:
                        self.login_signup()
                if event.type == pygame.KEYDOWN and self.Useractive or event.type == pygame.KEYDOWN and self.PassOneActive or event.type == pygame.KEYDOWN and self.PassTwoActive: #checks if typing and selected text box
                    if event.key == pygame.K_BACKSPACE and self.Useractive:
                        self.username = self.username[:-1]
                    elif event.key == pygame.K_BACKSPACE and self.PassOneActive:
                        self.passwordOne = self.passwordOne[:-1]
                    elif event.key == pygame.K_BACKSPACE and self.PassTwoActive:
                        self.passwordTwo = self.passwordTwo[:-1]

                    else:
                        self.win.box(0, self.win.point_five + 85, 510, 30)
                        if self.Useractive:
                            self.username += event.unicode
                        elif self.PassOneActive:
                            self.passwordOne += event.unicode
                        elif self.PassTwoActive:
                            self.passwordTwo += event.unicode

    def leader_choice(self):
        self.leader_choice_buttons = True
        self.win.fill()
        self.win.draw_leader_choice() #draws the leaderboard choice screen
        while self.running:
            for event in pygame.event.get():
                self.mouse = pygame.mouse.get_pos() #gets location of mouse
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.point_check(self.mouse, 1, 40):
                        self.leaderboard("df_high") #passes chosen leaderboard to next screen
                    if self.point_check(self.mouse, 2, 40):
                        self.leaderboard("prim_high")
                    if self.point_check(self.mouse, 7.7, 40):
                        self.menu()

    def leaderboard(self, x):
        self.leader_buttons = True
        self.win.fill()
        x = self.db.get_data(x)
        self.win.draw_leaderboard(x, self.user) #draws previously chosen leaderboard
        while self.running:
            for event in pygame.event.get():
                self.mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.point_check(self.mouse, 7.7, 40):
                        self.leader_buttons = False
                        self.leader_choice()

    def menu(self):
        self.main_menu_buttons = True
        self.running = True
        self.win.fill()
        self.win.draw_main_menu() #draws main menu
        while self.running:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos() #gets mouse position
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN: #checks if mouse pressed
                    if self.point_check(mouse, 1, 40):
                        self.main_menu_buttons = False
                        self.next = self.play #sets next screen to let user play
                        self.maze_menu() #goes to chosen next screen
                    elif self.point_check(mouse, 2, 40):
                        self.main_menu_buttons = False
                        self.next = self.solver_menu
                        self.maze_menu()
                    elif self.point_check(mouse, 3, 40):
                        self.main_menu_buttons = False
                        self.leader_choice()
                    elif self.point_check(mouse, 4, 40):
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()

    def maze_menu(self):
        self.db.cursor.execute(f"SELECT * FROM prim WHERE user = ?", (self.user,))
        self.win.draw_maze_menu()
        self.maze_menu_buttons = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.point_check(mouse, 2, 40):
                        self.maze_menu_buttons = False
                        self.maze_gen = Generator(50, self.win) #creates class to solve maze
                        self.maze_gen.depth_first_gen()  #generates maze
                        self.choice = 0 #stores choice of maze for leaderboard
                        self.mz = "df"
                        self.next("Depth First Generation")
                    if self.point_check(mouse, 3, 40):
                        self.main_menu_buttons = False
                        self.maze_gen = Generator(50, self.win)
                        self.maze_gen.prims()
                        self.choice = 1
                        self.mz = "prim"
                        self.next("Prims Generation")
                    if self.point_check(mouse, 6.7, 40):
                        self.main_menu_buttons = False
                        self.menu()

    def solver_menu(self, title_text):
        self.solver_menu_buttons = True
        self.win.draw_solver_menu(title_text)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.point_check(mouse, 1, 40):
                        self.solver_menu_buttons = False
                        self.solve = self.solver.solver #chosen solver solves the maze
                        self.maze()
                    if self.point_check(mouse, 2, 40):
                        self.solver_menu_buttons = False
                        self.solve = self.solver.breadth_first
                        self.maze()
                    if self.point_check(mouse, 3, 40):
                        self.solver_menu_buttons = False
                        self.solve = self.solver.a_star
                        self.maze()

                    if self.point_check(mouse, 4, 40):
                        self.solver_menu_buttons = False
                        self.maze_menu()

    def maze(self):
        self.maze_buttons = True
        self.win.draw_maze(self.maze_gen.Maze) #draws the maze
        time.sleep(1)
        self.solve(self.maze_gen.Maze) #algorithm solves maze
        time.sleep(1)
        self.win.transparent_fill()
        self.win.draw_button("Retry", 40, self.win.point_two)
        self.win.draw_button("Back", 40, self.win.point_three)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.MOUSEBUTTONDOWN: #checks if mouse been pressed
                    self.mouse = pygame.mouse.get_pos()
                    if self.point_check(self.mouse, 2, 40):
                        self.maze_buttons = False
                        self.maze_menu()
                    if self.point_check(self.mouse, 3, 40):
                        self.maze_buttons = False
                        self.menu()

    def play(self, title):
        self.db.cursor.execute(f"SELECT * FROM df WHERE user = ?", (self.user,))
        self.move = True
        self.play_buttons = True
        self.win.draw_maze(self.maze_gen.Maze)
        self.running = True
        self.x = 1
        self.y = 1
        self.comp = True
        self.start = time.time()
        while self.running:
        
            time.sleep(self.solver.sleep + 0.05)
            keys = pygame.key.get_pressed() #checks what key was pressed

            if self.maze_gen.Maze[self.x][self.y] == 3: #checks if players at end
                if self.comp:
                    self.end = time.time()
                    self.time = int(self.end) - int(self.start) #calculate how long taken
                    self.comp = False
                    self.win.draw_play_end(str(self.time)) #displays this
                    self.db.write_time(self.time, self.mz) #stores time in database
                else:
                    pass
                self.mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.point_check(self.mouse, 2, 40):
                            self.next("maze")
                        if self.point_check(self.mouse, 3, 40):
                            self.maze_menu()

            if keys[pygame.K_w]: #checks which direction player wants to move
                if 0 < self.x - 1 < len(self.maze_gen.Maze) and \
                        self.maze_gen.Maze[self.x - 1][self.y] != 1 and self.move: #checks player can move in direction
                    self.win.draw_player(self.x, self.y, self.x - 1, self.y) #moves player on screen
                    self.x -= 1
                else:
                    pass
            if keys[pygame.K_a]:
                if 0 < self.y - 1 < len(self.maze_gen.Maze) and \
                        self.maze_gen.Maze[self.x][self.y - 1] != 1:
                    self.win.draw_player(self.x, self.y, self.x, self.y - 1)
                    self.y -= 1
                else:
                    pass
            if keys[pygame.K_s]:
                if 0 < self.x + 1 < len(self.maze_gen.Maze) and \
                        self.maze_gen.Maze[self.x + 1][self.y] != 1 and self.move:
                    self.win.draw_player(self.x, self.y, self.x + 1, self.y)
                    self.x += 1
                else:
                    pass  #
            if keys[pygame.K_d]:
                if 0 < self.y + 1 < len(self.maze_gen.Maze) and \
                        self.maze_gen.Maze[self.x][self.y + 1] != 1:
                    self.win.draw_player(self.x, self.y, self.x, self.y + 1)
                    self.y += 1
                else:
                    pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()


men = Menu()
men.login_signup()
