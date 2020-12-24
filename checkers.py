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

def coords_to_circle(x, y):
    return [x * 64 + 32, y * 64 + 32]

def coords_to_square(x, y):
    return [x * 64, y * 64]

class Square:
    def __init__(self, colour, draw_coords, real_coords, piece):
        self.colour = colour
        self.draw_coords = draw_coords
        self.real_coords = real_coords
        self.piece = piece #0 means no piece, #1 means a white piece is there, #2 means a red piece is there      
    
    def draw(self):
        pygame.draw.rect(SCREEN, self.colour, self.draw_coords)

class Piece:
    def __init__(self, colour, draw_centre, coords, king):
        self.colour = colour
        self.draw_centre = draw_centre
        self.coords = coords
        self.king = king
    
    def update_draw_centre(self):
        self.draw_centre = coords_to_circle(self.coords)
    
    def draw(self):
        if self.colour == RED:
            pygame.draw.circle(SCREEN, RED, self.draw_centre, 24)
        if self.colour == WHITE:
            pygame.draw.circle(SCREEN, WHITE, self.draw_centre, 24)

    def available_moves(self):
        moves = []
        remove = []

        if self.colour == RED:
            if self.coords[0] > 0:
                moves.append([self, self.coords[0] - 1, self.coords[1] + 1])
            if self.coords[0] < 7:
                moves.append([self, self.coords[0] + 1, self.coords[1] + 1])
        
        if self.colour == WHITE:
            if self.coords[0] > 0:
                moves.append([self, self.coords[0] - 1, self.coords[1] - 1])
            if self.coords[0] < 7:
                moves.append([self, self.coords[0] + 1, self.coords[1] - 1])

        for move in moves: #To verify all moves are valid
            for square in dark_squares:
                if [move[1], move[2]] == square.real_coords and square.piece in (1, 2):
                    remove.append(move)
        for move in remove: #The remove list is needed as we can't remove items from a list as we're iterating it.
            moves.remove(move)
        for move in moves:
            pygame.draw.circle(SCREEN, BROWN, (move[1] * 64 + 32, move[2] * 64 + 32), 8)
        return moves

dark_squares = []# The only squares drawn were black ones as they're the only playable ones anyway. 
                #The background is white. The squares are found in a list, in order, from top to bottom, left to right

for collumn in range(0, 4):
    for row in range(1, 9, 2):
        dark_squares.append(Square(BLACK, (collumn * 128, row * 64, 64, 64), [2 * collumn, row], False))
    for row in range(0, 8, 2):
        dark_squares.append(Square(BLACK, (collumn * 128 + 64, row * 64, 64, 64), [2 * collumn + 1, row], False))

def board_draw():
    for item in dark_squares:
        item.draw()

def board_reset():
    pieces = []

    for square in dark_squares:
        if square.real_coords[1] <= 2:
            pieces.append(Piece(RED, [square.real_coords[0] * 64 + 32, square.real_coords[1] * 64 + 32], square.real_coords, 0))
            square.piece = True
        elif square.real_coords[1] >= 5:
            pieces.append(Piece(WHITE, [square.real_coords[0] * 64 + 32, square.real_coords[1] * 64 + 32], square.real_coords, 0))
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

    cursor_coords = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Right key pressed.")
                pieces[0].draw_centre[0] += 10
                pieces[0].draw()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in pieces: #Check if the cursor is hovering over a piece
                if cursor_coords[0] >= piece.draw_centre[0] - 32 and cursor_coords[0] <= piece.draw_centre[0] + 32 and cursor_coords[1] >= piece.draw_centre[1] - 32 and cursor_coords[1] <= piece.draw_centre[1] + 32:
                    board_draw()
                    pieces_draw(pieces)
                    moves = piece.available_moves()
            try:
                for move in moves: # Do a move. Do functions that turn real coords into draw coords automatically
                    if cursor_coords[0] > coords_to_square(move[1], move[2])[0] and cursor_coords[1] > coords_to_square(move[1], move[2])[1] and cursor_coords[0] < coords_to_square(move[1], move[2])[0] + 64 and cursor_coords[1] < coords_to_square(move[1], move[2])[1] + 64:
                        for square in dark_squares: #Make it so the square the piece is about to leave knows it no longuer has a piece
                            if square.real_coords == move[0].coords:
                                square.piece = False
                                board_draw()#board_draw() is needed instead of simply square_draw() as the other indication of possible movement (small purple circle), if present, also needs to be erased
                        
                        move[0].coords = [move[1], move[2]] #Give the piece new coordinates and draw it in its new place
                        move[0].draw_centre = coords_to_circle(move[1], move[2])
                        pieces_draw(pieces)

                        for square in dark_squares: #Make it so the square the piece is now on knows it has a piece
                            if square.real_coords == move[0].coords:
                                square.piece = True
            except:
                pass
        if event.type == pygame.QUIT: sys.exit()
