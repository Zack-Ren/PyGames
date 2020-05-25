import pygame

class playTicTacToe():
    def __init__(self):
        self.board = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
        ]

        self.X = 600
        self.Y = 740

        self.white = [255,255,255]
        self.black = [0, 0, 0]

        self.quitGame = False
        self.moveCounter = 0  #even = x, odd = o
        self.playing = True

        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.X,self.Y))
        self.gameDisplay.fill(self.white)
        self.drawGrid()
        pygame.display.set_caption("Tic-Tac-Toe")

        self.font = pygame.font.Font('Montserrat-Regular.ttf', 32)
        self.text = self.font.render('Tic Tac Toe', True, self.black, self.white)

        self.textRect = self.text.get_rect()
        self.textRect.center = (self.X // 2, 150 // 2)
        self.gameDisplay.blit(self.text, self.textRect)

        pygame.display.update()


        self.x_img = pygame.image.load("./images/x.png")
        self.o_img = pygame.image.load("./images/o.png")

        while not self.quitGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame = True
                    pygame.exit()
                    exit()
                if self.playing:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.x, self.y = pygame.mouse.get_pos()
                        print("x", self.x, "y", self.y)
                        if self.moveCounter % 2 == 0: #even = x
                            # self.text = self.font.render('Player 1 Turn', True, self.black, self.white)
                            # self.gameDisplay.blit(self.text, self.textRect)
                            # pygame.display.update()

                            self.player1_move(self.x, self.y)
                        else:
                            # self.text = self.font.render('Player 2 Turn', True, self.black, self.white)
                            # self.gameDisplay.blit(self.text, self.textRect)
                            # pygame.display.update()

                            self.player2_move(self.x, self.y)




    def drawGrid(self):
        pygame.draw.rect(self.gameDisplay, [0,0,0],(200,150,10,640))
        pygame.draw.rect(self.gameDisplay, [0,0,0],(400,150,10,640))
        pygame.draw.rect(self.gameDisplay, [0,0,0],(0,150,640,10))
        pygame.draw.rect(self.gameDisplay, [0,0,0],(0,350,640,10))
        pygame.draw.rect(self.gameDisplay, [0,0,0],(0,550,640,10))



    #   |1|2|3|
    #   |4|5|6|
    #   |7|8|9|


    def player1_move(self, x, y):
        if (0 < x < 200 and 160 < y < 350): #1
            if self.board[0][0] == 'x' or self.board[0][0] == 'o':
                return "Spot is filled"
            elif self.board[0][0] == '-':
                self.board[0][0] = 'x'
                self.gameDisplay.blit(self.x_img, (0,160))

            self.moveCounter += 1

        elif(210 < x < 400 and 160 < y < 350): #2
            if self.board[0][1] == 'x' or self.board[0][1] == 'o':
                return "Spot is filled"
            elif self.board[0][1] == '-':
                self.board[0][1] = 'x'
                self.gameDisplay.blit(self.x_img, (210,160))

            self.moveCounter += 1
        elif(410 < x < 640 and 160 < y < 350): #3
            if self.board[0][2] == 'x' or self.board[0][2] == 'o':
                return "Spot is filled"
            elif self.board[0][2] == '-':
                self.board[0][2] = 'x'
                self.gameDisplay.blit(self.x_img, (410,160))

            self.moveCounter += 1

        elif (0 < x < 200 and 360 < y < 550): #4
            if self.board[1][0] == 'x' or self.board[1][0] == 'o':
                return "Spot is filled"
            elif self.board[1][0] == '-':
                self.board[1][0] = 'x'
                self.gameDisplay.blit(self.x_img, (0,360))

            self.moveCounter += 1

        elif (210 < x < 400 and 360 < y < 550): #5
            if self.board[1][1] == 'x' or self.board[1][1] == 'o':
                return "Spot is filled"
            elif self.board[1][1] == '-':
                self.board[1][1] = 'x'
                self.gameDisplay.blit(self.x_img, (210,360))

            self.moveCounter += 1

        elif (410 < x < 640 and 360 < y < 550): #6
            if self.board[1][2] == 'x' or self.board[1][2] == 'o':
                return "Spot is filled"
            elif self.board[1][2] == '-':
                self.board[1][2] = 'x'
                self.gameDisplay.blit(self.x_img, (410,360))

            self.moveCounter += 1

        elif (0 < x < 200 and 560 < y < 770): #7
            if self.board[2][0] == 'x' or self.board[2][0] == 'o':
                return "Spot is filled"
            elif self.board[2][0] == '-':
                self.board[2][0] = 'x'
                self.gameDisplay.blit(self.x_img, (0,560))

            self.moveCounter += 1

        elif (210 < x < 400 and 560 < y < 770): #8
            if self.board[2][1] == 'x' or self.board[2][1] == 'o':
                return "Spot is filled"
            elif self.board[2][1] == '-':
                self.board[2][1] = 'x'
                self.gameDisplay.blit(self.x_img, (210,560))

            self.moveCounter += 1

        elif (410 < x < 640 and 560 < y < 770): #9
            if self.board[2][2] == 'x' or self.board[2][2] == 'o':
                return "Spot is filled"
            elif self.board[2][2] == '-':
                self.board[2][2] = 'x'
                self.gameDisplay.blit(self.x_img, (410,560))

            self.moveCounter += 1

        pygame.display.update()

        if self.checkWin():
            self.playing = False
            print("Game over. Player 1 wins!")
            self.text = self.font.render('Player 1 Wins!', True, self.black, self.white)
            self.gameDisplay.blit(self.text, self.textRect)
            pygame.display.update()

            return "Player 1"

        if not self.checkWin() and self.tie_game():
            self.playing = False
            print("Game over. Tie game")
            self.text = self.font.render('It\'s a Tie Game!', True, self.black, self.white)
            self.gameDisplay.blit(self.text, self.textRect)
            pygame.display.update()

            return "Tie Game"


        self.draw_board()

    def player2_move(self, x, y):
        if (0 < x < 200 and 160 < y < 350): #1
            if self.board[0][0] == 'x' or self.board[0][0] == 'o':
                return "Spot is filled"
            elif self.board[0][0] == '-':
                self.board[0][0] = 'o'
                self.gameDisplay.blit(self.o_img, (0,160))

            self.moveCounter += 1

        elif(210 < x < 400 and 160 < y < 350): #2
            if self.board[0][1] == 'x' or self.board[0][1] == 'o':
                return "Spot is filled"
            elif self.board[0][1] == '-':
                self.board[0][1] = 'o'
                self.gameDisplay.blit(self.o_img, (210,160))

            self.moveCounter += 1

        elif(410 < x < 640 and 160 < y < 350): #3
            if self.board[0][2] == 'x' or self.board[0][2] == 'o':
                return "Spot is filled"
            elif self.board[0][2] == '-':
                self.board[0][2] = 'o'
                self.gameDisplay.blit(self.o_img, (410,160))

            self.moveCounter += 1

        elif (0 < x < 200 and 360 < y < 550): #4
            if self.board[1][0] == 'x' or self.board[1][0] == 'o':
                return "Spot is filled"
            elif self.board[1][0] == '-':
                self.board[1][0] = 'o'
                self.gameDisplay.blit(self.o_img, (0,360))

            self.moveCounter += 1

        elif (210 < x < 400 and 360 < y < 550): #5
            if self.board[1][1] == 'x' or self.board[1][1] == 'o':
                return "Spot is filled"
            elif self.board[1][1] == '-':
                self.board[1][1] = 'o'
                self.gameDisplay.blit(self.o_img, (210,360))

            self.moveCounter += 1

        elif (410 < x < 640 and 360 < y < 550): #6
            if self.board[1][2] == 'x' or self.board[1][2] == 'o':
                return "Spot is filled"
            elif self.board[1][2] == '-':
                self.board[1][2] = 'o'
                self.gameDisplay.blit(self.o_img, (410,360))

            self.moveCounter += 1

        elif (0 < x < 200 and 560 < y < 770): #7
            if self.board[2][0] == 'x' or self.board[2][0] == 'o':
                return "Spot is filled"
            elif self.board[2][0] == '-':
                self.board[2][0] = 'o'
                self.gameDisplay.blit(self.o_img, (0,560))

            self.moveCounter += 1

        elif (210 < x < 400 and 560 < y < 770): #8
            if self.board[2][1] == 'x' or self.board[2][1] == 'o':
                return "Spot is filled"
            elif self.board[2][1] == '-':
                self.board[2][1] = 'o'
                self.gameDisplay.blit(self.o_img, (210,560))

            self.moveCounter += 1

        elif (410 < x < 640 and 560 < y < 770): #9
            if self.board[2][2] == 'x' or self.board[2][2] == 'o':
                return "Spot is filled"
            elif self.board[2][2] == '-':
                self.board[2][2] = 'o'
                self.gameDisplay.blit(self.o_img, (410,560))

            self.moveCounter += 1

        pygame.display.update()

        if self.checkWin():
            self.playing = False
            print("Game over. Player 2 wins!")
            self.text = self.font.render('Player 2 wins', True, self.black, self.white)
            self.gameDisplay.blit(self.text, self.textRect)
            pygame.display.update()

            return "Player 2"

        if not self.checkWin() and self.tie_game():
            self.playing = False
            print("Game over. Tie game")
            self.text = self.font.render('It\'s a Tie Game!', True, self.black, self.white)
            self.gameDisplay.blit(self.text, self.textRect)
            pygame.display.update()

            return "Tie Game"

        pygame.display.update()
        self.draw_board()

    def draw_board(self):
        for i in range(3):
            print(self.board[i])


    def tie_game(self):
        counter = 0

        for b in self.board:
            counter = b.count("-") + counter

        return counter == 0


    def checkWin(self):
        for y in self.board:
            if y[0] == y[1] == y[2] and y[0] != "-":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "-":
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] != "-" :
            return True

        for x in range(3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] and self.board[0][x] != '-':
                return True

        else:
            return False

playTicTacToe()

