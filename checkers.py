import pygame, sys

pygame.init()
pygame.display.set_caption("Checkers")

SIZE = width, height = 512, 512
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREY = 128, 128, 128
RED = 255, 0, 0

SCREEN = pygame.display.set_mode(SIZE)

class Square:
    def __init__(self, colour, coords):
        self.colour = colour
        self.coords = coords
    
    def draw(self):
        pygame.draw.rect(SCREEN, self.colour, self.coords)

b8_1 = Square(BLACK, (64, 0, 64, 64))

def board_draw():
    w8_1 = Square(WHITE, (0, 0, 64, 64))
    w8_1.draw()
    w8_2 = Square(WHITE, (128, 0, 64, 64))
    w8_2.draw()
    w8_3 = Square(WHITE, (256, 0, 64, 64))
    w8_3.draw()
    w8_4 = Square(WHITE, (384, 0, 64, 64))
    w8_4.draw()
    b8_1 = Square(BLACK, (64, 0, 64, 64))
    b8_1.draw()
    b8_2 = Square(BLACK, (192, 0, 64, 64))
    b8_2.draw()
    b8_3 = Square(BLACK, (320, 0, 64, 64))
    b8_3.draw()
    b8_4 = Square(BLACK, (448, 0, 64, 64))
    b8_4.draw()

    b7_1 = Square(BLACK, (0, 64, 64, 64))
    b7_1.draw()
    b7_2 = Square(BLACK, (128, 64, 64, 64))
    b7_2.draw()
    b7_3 = Square(BLACK, (256, 64, 64, 64))
    b7_3.draw()
    b7_4 = Square(BLACK, (384, 64, 64, 64))
    b7_4.draw()
    w7_1 = Square(WHITE, (64, 64, 64, 64))
    w7_1.draw()
    w7_2 = Square(WHITE, (192, 64, 64, 64))
    w7_2.draw()
    w7_3 = Square(WHITE, (320, 64, 64, 64))
    w7_3.draw()
    w7_4 = Square(WHITE, (448, 64, 64, 64))
    w7_4.draw()

    w6_1 = Square(WHITE, (0, 128, 64, 64))
    w6_1.draw()
    w6_2 = Square(WHITE, (128, 128, 64, 64))
    w6_2.draw()
    w6_3 = Square(WHITE, (256, 128, 64, 64))
    w6_3.draw()
    w6_4 = Square(WHITE, (384, 128, 64, 64))
    w6_4.draw()
    b6_1 = Square(BLACK, (64, 128, 64, 64))
    b6_1.draw()
    b6_2 = Square(BLACK, (192, 128, 64, 64))
    b6_2.draw()
    b6_3 = Square(BLACK, (320, 128, 64, 64))
    b6_3.draw()
    b6_4 = Square(BLACK, (448, 128, 64, 64))
    b6_4.draw()

    b5_1 = Square(BLACK, (0, 192, 64, 64))
    b5_1.draw()
    b5_2 = Square(BLACK, (128, 192, 64, 64))
    b5_2.draw()
    b5_3 = Square(BLACK, (256, 192, 64, 64))
    b5_3.draw()
    b5_4 = Square(BLACK, (384, 192, 64, 64))
    b5_4.draw()
    w5_1 = Square(WHITE, (64, 192, 64, 64))
    w5_1.draw()
    w5_2 = Square(WHITE, (192, 192, 64, 64))
    w5_2.draw()
    w5_3 = Square(WHITE, (320, 192, 64, 64))
    w5_3.draw()
    w5_4 = Square(WHITE, (448, 192, 64, 64))
    w5_4.draw()

    w4_1 = Square(WHITE, (0, 256, 64, 64))
    w4_1.draw()
    w4_2 = Square(WHITE, (128, 256, 64, 64))
    w4_2.draw()
    w4_3 = Square(WHITE, (256, 256, 64, 64))
    w4_3.draw()
    w4_4 = Square(WHITE, (384, 256, 64, 64))
    w4_4.draw()
    b4_1 = Square(BLACK, (64, 256, 64, 64))
    b4_1.draw()
    b4_2 = Square(BLACK, (192, 256, 64, 64))
    b4_2.draw()
    b4_3 = Square(BLACK, (320, 256, 64, 64))
    b4_3.draw()
    b4_4 = Square(BLACK, (448, 256, 64, 64))
    b4_4.draw()

    b3_1 = Square(BLACK, (0, 320, 64, 64))
    b3_1.draw()
    b3_2 = Square(BLACK, (128, 320, 64, 64))
    b3_2.draw()
    b3_3 = Square(BLACK, (256, 320, 64, 64))
    b3_3.draw()
    b3_4 = Square(BLACK, (384, 320, 64, 64))
    b3_4.draw()
    w3_1 = Square(WHITE, (64, 320, 64, 64))
    w3_1.draw()
    w3_2 = Square(WHITE, (192, 320, 64, 64))
    w3_2.draw()
    w3_3 = Square(WHITE, (320, 320, 64, 64))
    w3_3.draw()
    w3_4 = Square(WHITE, (448, 320, 64, 64))
    w3_4.draw()

    w2_1 = Square(WHITE, (0, 384, 64, 64))
    w2_1.draw()
    w2_2 = Square(WHITE, (128, 384, 64, 64))
    w2_2.draw()
    w2_3 = Square(WHITE, (256, 384, 64, 64))
    w2_3.draw()
    w2_4 = Square(WHITE, (384, 384, 64, 64))
    w2_4.draw()
    b2_1 = Square(BLACK, (64, 384, 64, 64))
    b2_1.draw()
    b2_2 = Square(BLACK, (192, 384, 64, 64))
    b2_2.draw()
    b2_3 = Square(BLACK, (320, 384, 64, 64))
    b2_3.draw()
    b2_4 = Square(BLACK, (448, 384, 64, 64))
    b2_4.draw()

    b1_1 = Square(BLACK, (0, 448, 64, 64))
    b1_1.draw()
    b1_2 = Square(BLACK, (128, 448, 64, 64))
    b1_2.draw()
    b1_3 = Square(BLACK, (256, 448, 64, 64))
    b1_3.draw()
    b1_4 = Square(BLACK, (384, 448, 64, 64))
    b1_4.draw()
    w1_1 = Square(WHITE, (64, 448, 64, 64))
    w1_1.draw()
    w1_2 = Square(WHITE, (192, 448, 64, 64))
    w1_2.draw()
    w1_3 = Square(WHITE, (320, 448, 64, 64))
    w1_3.draw()
    w1_4 = Square(WHITE, (448, 448, 64, 64))
    w1_4.draw()

class RedPiece:
    def __init__(self, colour, centre, king):
        self.colour = colour
        self.centre = centre
        self.king = king
    
    def draw(self):
        pygame.draw.circle(SCREEN, RED, self.centre, 24)

class WhitePiece:
    def __init__(self, colour, coords, king):
        self.colour = colour
        self.coords = coords
        self.king = king

test_red_piece = RedPiece(RED, (96, 32), False)

while True:
    SCREEN.fill(GREY)
    board_draw()
    test_red_piece.draw()
    pygame.display.update()

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    if mouse_x >= b8_1.coords[0] and mouse_x <= b8_1.coords[0] + 64 and mouse_y >= b8_1.coords[1] and mouse_y <= b8_1.coords[1] + 64:
        print("Interacting with ")
        print("piece.")

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()