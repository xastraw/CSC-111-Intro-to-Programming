import pygame

class Hud:

    def __init__(self, GameWindow, WindowSize, titleFontFile, mainFontFile):
        self.score = 0
        self.health = 0
        self.level = 1
        self.gameWindow = GameWindow
        self.windowSize = WindowSize
        self.titleSize = 64
        self.mainSize = 32
        self.titleFont = pygame.font.Font(titleFontFile, self.titleSize)
        self.mainFont = pygame.font.Font(mainFontFile, self.mainSize)

    def main_menu(self, text, color, x_offset=0, y_offset=0):
        titleText = self.titleFont.render(text, True, color)
        titleTextRect = titleText.get_rect()
        titleTextRect.center = self.windowSize[0] / 2 + x_offset, self.windowSize[1] / 2 + y_offset
        self.gameWindow.blit(titleText, titleTextRect)

    def game_info(self, scoreLocation=0, levelLocation=0, livesLocation=0):
        scoreString = f"Score: {self.score}"
        scoreText = self.mainFont.render(scoreString, True, "purple")
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.topleft = 8, 8
        self.gameWindow.blit(scoreText, scoreTextRect)

        healthString = "Health: " + str(self.health)
        healthText = self.mainFont.render(healthString, True, (140,9,0))
        healthTextRect = healthText.get_rect()
        healthTextRect.topleft= 190, 8
        self.gameWindow.blit(healthText, healthTextRect)
    
    def game_end(self, text, color, x_offset=0, y_offset=0):
        titleText = self.titleFont.render(text, True, color)
        titleTextRect = titleText.get_rect()
        titleTextRect.center = self.windowSize[0] / 2 + x_offset, self.windowSize[1] / 2 + y_offset
        self.gameWindow.blit(titleText, titleTextRect)
    
    def place_text(self, text, color, x_offset, y_offset):
        mainText = self.mainFont.render(text, True, color)
        mainTextRect = mainText.get_rect()
        mainTextRect.center = self.windowSize[0] / 2 + x_offset, self.windowSize[1] / 2 + y_offset
        self.gameWindow.blit(mainText, mainTextRect)