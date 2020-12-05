import pygame, sys

pygame.init()
pygame.display.set_caption("Checkers")

SIZE = width, height = 512, 512
BLACK = 0, 0, 0
GREY = 200, 200, 200
RED = 255, 0, 0
WHITE = 255, 255, 255
BROWN = 128, 0, 0

SCREEN = pygame.display.set_mode(SIZE)

class Square:
    def __init__(self, colour, coords):
        self.colour = colour
        self.coords = coords
    
    def draw(self):
        pygame.draw.rect(SCREEN, self.colour, self.coords)

class RedPiece:
    def __init__(self, colour, centre, king):
        self.colour = colour
        self.centre = centre
        self.king = king
    
    def draw(self):
        pygame.draw.circle(SCREEN, RED, self.centre, 24)
    
    def available_moves(self):
        moves = []
        if self.centre[0] > 32:
            moves.append((self.centre[0] - 64, self.centre[1] + 64))
            pygame.draw.circle(SCREEN, BROWN, (self.centre[0] - 64, self.centre[1] + 64), 8)
        if self.centre[0] < 480:
            moves.append((self.centre[0] + 64, self.centre[1] + 64))
            pygame.draw.circle(SCREEN, BROWN, (self.centre[0] + 64, self.centre[1] + 64), 8)
        return moves

class WhitePiece:
    def __init__(self, colour, centre, king):
        self.colour = colour
        self.centre = centre
        self.king = king
    
    def draw(self):
        pygame.draw.circle(SCREEN, WHITE, self.centre, 24)
    
    def available_moves(self):
        moves = []
        if self.centre[0] > 32:
            moves.append((self.centre[0] - 64, self.centre[1] - 64))
            pygame.draw.circle(SCREEN, BROWN, (self.centre[0] - 64, self.centre[1] - 64), 8)
        if self.centre[0] < 480:
            moves.append((self.centre[0] + 64, self.centre[1] - 64))
            pygame.draw.circle(SCREEN, BROWN, (self.centre[0] + 64, self.centre[1] - 64), 8)
        return moves

b8_1 = Square(BLACK, (64, 0, 64, 64))

dark_squares = []# The only squares drawn were black ones as they're the only playable ones anyway. The background is white. The squares are found in a list, in order, from top to bottom, left to right

for collumn in range(0, 4):
    for row in range(1, 9, 2):
        dark_squares.append(Square(BLACK, (collumn * 128, row * 64, 64, 64)))
    for row in range(0, 8, 2):
        dark_squares.append(Square(BLACK, (collumn * 128 + 64, row * 64, 64, 64)))

print(dark_squares[3].coords[0])

def board_draw():

    for item in dark_squares:
        item.draw()

def board_reset():
    red_pieces = []
    white_pieces = []

    for item in dark_squares:
        if item.coords[1] <= 128:
            red_pieces.append(RedPiece(RED, (item.coords[0] + 32, item.coords[1] + 32), False))
    
    for red_piece in red_pieces:
        red_piece.draw()
    
    for item in dark_squares:
        if item.coords[1] >= 320:
            white_pieces.append(WhitePiece(WHITE, (item.coords[0] + 32, item.coords[1] + 32), False))
    
    for white_piece in white_pieces:
        white_piece.draw()

    return red_pieces, white_pieces

def pieces_draw(pieces):
    for piece in pieces:
        piece.draw()

test_red_piece = RedPiece(RED, (96, 32), False)

SCREEN.fill(GREY)
board_draw()
red_pieces, white_pieces = board_reset()

while True:
    pygame.display.update()

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    for piece in red_pieces:
        if mouse_x >= piece.centre[0] - 32 and mouse_x <= piece.centre[0] + 32 and mouse_y >= piece.centre[1] - 32 and mouse_y <= piece.centre[1] + 32:
            board_draw()
            pieces_draw(red_pieces + white_pieces)
            piece.available_moves()

    for piece in white_pieces:
        if mouse_x >= piece.centre[0] - 32 and mouse_x <= piece.centre[0] + 32 and mouse_y >= piece.centre[1] - 32 and mouse_y <= piece.centre[1] + 32:
            board_draw()
            pieces_draw(red_pieces + white_pieces)
            piece.available_moves()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
