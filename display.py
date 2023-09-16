import pygame
import sys

class Display:
    def __init__(self, grid_size=(8, 8), cell_size=8):
        pygame.init()
        self.GRID_SIZE = grid_size
        self.CELL_SIZE = cell_size
        self.GRID_WIDTH = self.GRID_SIZE[0] * self.CELL_SIZE
        self.GRID_HEIGHT = self.GRID_SIZE[1] * self.CELL_SIZE
        self.SCREEN_WIDTH = self.GRID_WIDTH
        self.SCREEN_HEIGHT = self.GRID_HEIGHT
        self.tick = 0   
        self.COLORS = {
            'BLACK': (0, 0, 0),
            'WHITE': (255, 255, 255),
            'RED': (136, 0, 0),
            'CYAN': (170, 255, 238),
            'PURPLE': (204, 68, 204),
            'GREEN': (0, 204, 85),
            'BLUE': (0, 0, 170),
            'YELLOW': (238, 238, 119),
            'ORANGE': (221, 136, 85),
            'BROWN': (102, 68, 0),
            'LIGHT_RED': (255, 119, 119),
            'DARK_GREY': (51, 51, 51),
            'GREY': (119, 119, 119),
            'LIGHT_GREEN': (170, 255, 102),
            'LIGHT_BLUE': (0, 136, 255),
            'LIGHT_GREY': (187, 187, 187),
        }
        
        self.current_fg_color = self.COLORS['LIGHT_BLUE']
        self.current_bg_color = self.COLORS['BLUE']
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("EmuDisplay")
        self.clock = pygame.time.Clock()
        self.grid = [[' ' for _ in range(self.GRID_SIZE[0])] for _ in range(self.GRID_SIZE[1])]
        self.emulation_running = True
        self.paused = False
        self.unicode_font = pygame.font.Font("fonts/c64.ttf", 16)

    def set_char_in_cell(self, row, col, char):
        if 0 <= row < self.GRID_SIZE[1] and 0 <= col < self.GRID_SIZE[0]:
            self.grid[row][col] = char

    def set_fg_color(self, color):
        if color in self.COLORS:
            self.current_fg_color = self.COLORS[color]

    def set_bg_color(self, color):
        if color in self.COLORS:
            self.current_bg_color = self.COLORS[color]

    def draw_grid(self):
        for row in range(self.GRID_SIZE[1]):
            for col in range(self.GRID_SIZE[0]):
                cell_rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                pygame.draw.rect(self.screen, self.current_bg_color, cell_rect)
                cell_char = self.grid[row][col]
                if cell_char != ' ':
                    cell_text = self.unicode_font.render(cell_char, True, self.current_fg_color)
                    text_rect = cell_text.get_rect(topleft=cell_rect.topleft)
                    self.screen.blit(cell_text, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self, program_function):
        while True:
            self.handle_events()
            if not self.paused:
                program_function(self)
            self.screen.fill(self.current_bg_color)
            self.draw_grid()
            
            pygame.display.flip()
            self.clock.tick(self.tick)

def grid(display):
    display.set_fg_color('RED')
    display.set_bg_color('YELLOW')
    
    for row in range(display.GRID_SIZE[1]):
        for col in range(display.GRID_SIZE[0]):
            display.set_char_in_cell(row, col, 'A')
