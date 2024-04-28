import pygame #modul python
pygame.init()
pygame.font.init()

RED = (255, 0, 0)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('SoldierFont.ttf', size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
