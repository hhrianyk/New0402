import pygame
import sys

pygame.init()

width, height = 1000, 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Мое окно Pygame")

background_image = pygame.image.load("fon2.jpg")

card1_image = pygame.image.load("img1.png")
card2_image = pygame.image.load("img2.png")

card1_position = (-50, 200)
card2_position = (400, 200)

size_card1 = (700, 700)
size_card2 = (700, 700)

card1_image = pygame.transform.scale(card1_image, size_card1)
card2_image = pygame.transform.scale(card2_image, size_card2)

font = pygame.font.Font(None, 36)

default_text = "Кликните на карточку"
card1_text = "Текст карточки 1"
card2_text = "Текст карточки 2"

current_text = default_text

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if card1_position[0] <= mouse_x <= card1_position[0] + size_card1[0] and \
                    card1_position[1] <= mouse_y <= card1_position[1] + size_card1[1]:
                current_text = card1_text
            elif card2_position[0] <= mouse_x <= card2_position[0] + size_card2[0] and \
                    card2_position[1] <= mouse_y <= card2_position[1] + size_card2[1]:
                current_text = card2_text
            else:
                current_text = default_text

    screen.blit(background_image, (0, 0))
    screen.blit(card1_image, card1_position)
    screen.blit(card2_image, card2_position)
    text = font.render(current_text, True, (255, 255, 255))
    screen.blit(text, (50, 50))
    pygame.display.flip()