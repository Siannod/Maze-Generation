import pygame

class Window:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen
        self.blockx = 10  # finds how wide each block must be
        self.blocky = 10  # find how tall each block must be
        self.smallfont = pygame.font.SysFont('freesansbold.ttf', 35)
        self.usertext = pygame.font.SysFont("freesansbold.ttf", 27)
        self.labelfont = pygame.font.SysFont("freesansbold.ttf", 20)
        self.loginFont = pygame.font.SysFont("freesansbold.ttf", 25)
        self.timeFont = pygame.font.SysFont("freesansbold.ttf", 50)
        self.color = (200, 200, 200)
        self.width = self.height = 510
        self.point_one = 125
        self.point_two = 180
        self.point_three = 235
        self.point_four = 290
        self.point_five = 345
        self.point_six = 405
        self.point_seven = 455
        self.player_col = (1, 50, 32)

    def draw_maze(self, maze): #takes 2D array y draws it on the screen
        self.maze = maze
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 0:
                    pygame.draw.rect(self.screen, (200, 200, 200),
                                     pygame.Rect(j * self.blockx, i * self.blocky, self.blockx, self.blocky))
                elif self.maze[i][j] == 1:
                    pygame.draw.rect(self.screen, (50, 50, 50),
                                     pygame.Rect(j * self.blockx, i * self.blocky, self.blockx, self.blocky))
                elif self.maze[i][j] == 2:
                    pygame.draw.rect(self.screen, (0, 255, 0),
                                     pygame.Rect(j * self.blockx, i * self.blocky, self.blockx, self.blocky))
                else:
                    pygame.draw.rect(self.screen, (255, 0, 0),
                                     pygame.Rect(j * self.blockx, i * self.blocky, self.blockx, self.blocky))
        pygame.draw.rect(self.screen, (50, 50, 50), pygame.Rect(0, 50 * self.blocky, self.blockx * 51, self.blocky))
        pygame.draw.rect(self.screen, (50, 50, 50), pygame.Rect(50 * self.blockx, 0, self.blockx, self.blocky * 51))
        pygame.display.flip()

    def draw_cell(self, x, y, type):
        if type == 1:
            pygame.draw.rect(self.screen, (200, 200, 200),
                             pygame.Rect(x * self.blockx, y * self.blocky, self.blockx, self.blocky))
        else:
            pygame.draw.rect(self.screen, (50, 50, 50),
                             pygame.Rect(x * self.blockx, y * self.blocky, self.blockx, self.blocky))

    def draw_solver(self, x, y):
        pygame.draw.rect(self.screen, (50, 50, 200), pygame.Rect(10 * y, 10 * x, 10, 10))
        pygame.display.flip()

    def clear_solver(self, x, y):
        pygame.draw.rect(self.screen, (200, 50, 50), pygame.Rect(10 * y, 10 * x, 10, 10))
        pygame.display.flip()

    def flip(self):
        pygame.display.flip()

    def draw_title(self, text):
        pygame.draw.rect(self.screen, (50, 50, 50), [20, 50, 470, 50])
        self.MAZE_TEXT = self.smallfont.render(text, True, self.color)
        self.MT_rect = self.MAZE_TEXT.get_rect(center=(510 / 2, 80))
        self.screen.blit(self.MAZE_TEXT, self.MT_rect)
        self.flip()

    def draw_button(self, buttontext, x, y, lenbon=0):
        pygame.draw.rect(self.screen, (50, 50, 50), [x, y, 430 + lenbon, 40])
        self.button_text = self.smallfont.render(buttontext, True, self.color)
        self.BT_rect = self.button_text.get_rect(center=(510 / 2, y + 20))
        self.screen.blit(self.button_text, self.BT_rect)
        self.flip()

    def big_button(self, buttontext, x, y):
        pygame.draw.rect(self.screen, (50, 50, 50), [x, y, 430, 60])
        self.button_text = self.smallfont.render(buttontext, True, self.color)
        self.BT_rect = self.button_text.get_rect(center=(510 / 2, y + 30))
        self.screen.blit(self.button_text, self.BT_rect)
        self.flip()

    def draw_label(self, x, y, text, bon=0):
        pygame.draw.rect(self.screen, (50, 50, 50), [x, y, 100 + bon, 20])
        self.button_text = self.labelfont.render(text, True, self.color)
        self.BT_rect = self.button_text.get_rect(topleft=(x +5, y + 5))
        self.screen.blit(self.button_text, self.BT_rect)
        self.flip()

    def draw_score(self, x, y, text, count, color, bon=0):
        self.text_wdith, self.text_height = self.labelfont.size(text)
        pygame.draw.rect(self.screen, color, [x, y, 100 + bon, 30])
        self.button_text = self.labelfont.render(text, True, self.color)
        self.BT_rect = self.button_text.get_rect(center=(x + 75, self.point_two + (count * 35) +15))
        self.screen.blit(self.button_text, self.BT_rect)
        self.flip()

    def draw_login_button(self, x, y, text):
        pygame.draw.rect(self.screen, (50, 50, 50), [x, y + 20, 100, 60])
        self.button_text = self.loginFont.render(text, True, self.color)
        self.BT_rect = self.button_text.get_rect(center=(510 / 2, y + 50))
        self.screen.blit(self.button_text, self.BT_rect)
        self.flip()

    def draw_text(self, x, y, text):
        self.button_text = self.labelfont.render(text, True, (255, 0, 0))
        self.BT_rect = self.button_text.get_rect(center=(510 / 2, y + 50))
        self.screen.blit(self.button_text, self.BT_rect)
        self.flip()

    def draw_subtitle(self, x, y, text):
        self.text = self.smallfont.render(str(text), True, self.color)
        self.sub_rect = self.text.get_rect(center=(x + 102, y + 30))
        pygame.draw.rect(self.screen, (50, 50, 50), [x, y, 205, 50])
        self.screen.blit(self.text, self.sub_rect)

    def draw_main_menu(self):
        self.screen.fill((0, 0, 0))
        self.draw_title("MAZE GENERATOR")
        self.draw_button("Play", 40, self.point_one)
        self.draw_button("View Solver", 40, self.point_two)
        self.draw_button("Leaderboard", 40, self.point_three)
        self.draw_button("Quit", 40, self.point_four)

    def draw_maze_menu(self):
        self.screen.fill((0, 0, 0))
        self.draw_title("MAZE GENERATOR")
        self.draw_button("Depth First Generation", 40, self.point_two)
        self.draw_button("Prims Generation", 40, self.point_three)

        self.draw_button("Back", 40, self.point_six)

    def draw_solver_menu(self, title_text):
        self.screen.fill((0, 0, 0))
        self.draw_title(title_text)
        self.draw_button("Depth First Solver", 40, self.point_one)
        self.draw_button("Breadth First Solver", 40, self.point_two)
        self.draw_button("A Star Solver", 40, self.point_three)
        self.draw_button("Back", 40, self.point_four)

    def draw_login_signup(self):
        self.big_button("LOGIN", 40, self.point_one)
        self.big_button("SIGN UP", 40, self.point_three)

    def draw_login(self, Utext, Ptext):

        self.draw_title("Login")

        self.draw_label(40, self.point_one, "Username")
        self.draw_label(40, self.point_three, "Password")
        self.draw_text_box(40, self.point_one, Utext)
        self.draw_text_box(40, self.point_three, Ptext)
        self.draw_login_button(205, self.point_four, "Login")
        self.draw_button("Back", 100, self.point_six, -125)

    def failed_login(self):
        self.draw_text(510 / 2, self.point_four - 40, "USERNAME/PASSWORD INCORRECT")
        self.flip()

    def user_taken(self):
        self.draw_text(510 / 2, self.point_one + 15, "USERNAME IN USE")
        self.flip()

    def pass_error(self):
        self.draw_text(510 / 2, self.point_four, "PASSWORDS DO NOT MATCH")
        self.flip()

    def draw_signup(self, user, passOne, passTwo):
        self.draw_title("Signup")
        self.draw_label(40, self.point_one, "Username")
        self.draw_label(40, self.point_three - 20, "Password")
        self.draw_label(40, self.point_four - 20, "Re-Enter Password", 65)
        self.draw_text_box(40, self.point_one, user)
        self.draw_text_box(40, self.point_three - 20, passOne)
        self.draw_text_box(40, self.point_four - 20, passTwo)
        self.draw_login_button(205, self.point_five, "Signup")
        self.draw_button("Back", 100, self.point_seven, -125)

        self.flip()

    def draw_text_box(self, x, y, text):
        self.login_rect = [x, y + 20, 430, 30]
        self.login_rect = [x, y + 20, 430, 30]
        pygame.draw.rect(self.screen, (200, 200, 200), self.login_rect)
        self.user_text = self.usertext.render(text, True, (50, 50, 50))
        self.BT_rect = self.user_text.get_rect(midleft=(50, y + 35))
        self.screen.blit(self.user_text, self.BT_rect)
        pygame.display.flip()

    def draw_leader_choice(self):
        self.draw_title("Choose Leaderboard")
        self.draw_button("Depth First", 40, self.point_one)
        self.draw_button("Prims", 40, self.point_two)
        self.draw_button("Back", 40, self.point_seven)

    def draw_leaderboard(self, highscores, user):
        self.draw_title("LEADERBOARD")
        self.draw_subtitle(45, self.point_one, "User")
        count = 0
        for key in highscores:
            if key[0] == user:
                self.draw_score(75, self.point_two + (count * 35), key[0], count, self.player_col, 50 )
            else:
                self.draw_score(75, self.point_two + (count * 35), key[0], count, (50, 50, 50), 50 )
            count += 1
        self.draw_subtitle(270, self.point_one, "Time")
        count = 0
        for key in highscores:
            if key[0] == user:
                self.draw_score(300, self.point_two + (count * 35), str(key[1]), count, self.player_col, 50)
            else:
                self.draw_score(300, self.point_two + (count * 35), str(key[1]), count, (50, 50, 50), 50)

            count += 1
        self.draw_button("Back", 100, self.point_seven, -125)
        self.flip()

    def transparent_fill(self):
        self.full_image = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.full_image, (0, 0, 0), self.full_image.get_rect(), 10)
        self.full_image.set_alpha(200)
        self.screen.blit(self.full_image, (0, 0))
        self.flip()

    def draw_time(self, text):
        self.button_text = self.timeFont.render(str(text), True, (255, 0, 0))
        self.BT_rect = self.button_text.get_rect(center=(510 / 2, self.point_one))
        self.screen.blit(self.button_text, self.BT_rect)
        self.flip()

    def draw_player(self, x, y, newx, newy):
        pygame.draw.rect(self.screen, (200, 200, 200),
                         pygame.Rect(y * self.blockx, x * self.blocky, self.blockx, self.blocky))
        pygame.draw.rect(self.screen, (50, 200, 50),
                         pygame.Rect(newy * self.blockx, newx * self.blocky, self.blockx, self.blocky))
        self.flip()

    def fill(self):
        self.screen.fill((0, 0, 0))

    def box(self, x, y, lens, dep):
        pygame.draw.rect(self.screen, (0, 0, 0), [x, y, lens, dep])

    def draw_play_end(self, time):
        self.transparent_fill()
        self.draw_time(str(time))
        self.draw_button("Retry", 40, self.point_two)
        self.draw_button("Back", 40, self.point_three)

