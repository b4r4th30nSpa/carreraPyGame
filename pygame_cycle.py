#ciclo de 3 fases:
#pintar objetos en pantalla, gestionar eventos(puede implicar modificar objetos),
#y vuelta a empezar: actualizar ('repintar') objetos en pantalla

import pygame, sys

width =640
height = 480

screen = pygame.display.set_mode((width, height))
screen.fill((246,147,48))
pygame.display.set_caption('Ciclo básico de PyGame')
pygame.init()

gameOver = False

while not gameOver:
    for event in pygame.event.get():  #pygame.event.get() es un buffer que contiene un iterable de eventos ocurridos
        if event.type == pygame.QUIT:
            gameOver = True
    pygame.display.flip() #o equivantemente: pygame.display.update()

pygame.quit() #salir de PyGame
sys.exit() #salir de Python (????)       
    
