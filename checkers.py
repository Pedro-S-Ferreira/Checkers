import pygame, sys

pygame.init()
pygame.display.set_caption("Checkers")

SIZE = width, height = 512, 512
BLACK = 0, 0, 0
GREY = 200, 200, 200
RED = 255, 0, 0
WHITE = 255, 255, 255
BROWN = 200, 0, 200

SCREEN = pygame.display.set_mode(SIZE)

class Square:
    def __init__(self, colour, draw_coords, real_coords, piece):
        self.colour = colour
        self.draw_coords = draw_coords
        self.real_coords = real_coords
        self.piece = False      
    
    def draw(self):
        pygame.draw.rect(SCREEN, self.colour, self.draw_coords)

class Piece:
    def __init__(self, colour, draw_centre, coords, king):
        self.colour = colour
        self.draw_centre = draw_centre
        self.coords = coords
        self.king = king
    
    def draw(self):
        if self.colour == RED:
            pygame.draw.circle(SCREEN, RED, self.draw_centre, 24)
        if self.colour == WHITE:
            pygame.draw.circle(SCREEN, WHITE, self.draw_centre, 24)
    def available_moves(self):

        if self.colour == RED:
            moves = []
            if self.coords[0] >= 0:
                for square in dark_squares:
                    if square.real_coords == self.coords:#fix this
                        moves.append((self.coords[0] - 1, self.coords[1] + 1))
                        pygame.draw.circle(SCREEN, BROWN, (self.draw_centre[0] - 64, self.draw_centre[1] + 64), 8)
            if self.coords[0] < 7:
                moves.append((self.coords[0] + 1, self.coords[1] + 1))
                pygame.draw.circle(SCREEN, BROWN, (self.draw_centre[0] + 64, self.draw_centre[1] + 64), 8)
            return moves
        
        if self.colour == WHITE:
            moves = []
            if self.coords[0] >= 0:
                moves.append((self.coords[0] - 1, self.coords[1] - 1))
                pygame.draw.circle(SCREEN, BROWN, (self.draw_centre[0] - 64, self.draw_centre[1] - 64), 8)
            if self.coords[0] < 7:
                moves.append((self.coords[0] + 1, self.coords[1] - 1))
                pygame.draw.circle(SCREEN, BROWN, (self.draw_centre[0] + 64, self.draw_centre[1] - 64), 8)
            return moves

dark_squares = []# The only squares drawn were black ones as they're the only playable ones anyway. 
                #The background is white. The squares are found in a list, in order, from top to bottom, left to right

for collumn in range(0, 4):
    for row in range(1, 9, 2):
        dark_squares.append(Square(BLACK, (collumn * 128, row * 64, 64, 64), (collumn, row), False))
    for row in range(0, 8, 2):
        dark_squares.append(Square(BLACK, (collumn * 128 + 64, row * 64, 64, 64), (collumn, row), False))

def board_draw():
    for item in dark_squares:
        item.draw()

def board_reset():
    pieces = []

    for square in dark_squares:
        if square.real_coords[1] <= 2:
            pieces.append(Piece(RED, (square.draw_coords[0] + 32, square.draw_coords[1] + 32), square.real_coords, False))
            square.piece = True
        elif square.real_coords[1] >= 5:
            pieces.append(Piece(WHITE, (square.draw_coords[0] + 32, square.draw_coords[1] + 32), square.real_coords, False))
            square.piece = True
    
    for piece in pieces:
        piece.draw()

    return pieces

def pieces_draw(pieces):
    for piece in pieces:
        piece.draw()

SCREEN.fill(GREY)
board_draw()
pieces = board_reset()

while True:
    pygame.display.update()

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    for piece in pieces: #Check if the cursor is hovering over a piece
        if mouse_x >= piece.draw_centre[0] - 32 and mouse_x <= piece.draw_centre[0] + 32 and mouse_y >= piece.draw_centre[1] - 32 and mouse_y <= piece.draw_centre[1] + 32:
            board_draw()
            pieces_draw(pieces)
            piece.available_moves()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
