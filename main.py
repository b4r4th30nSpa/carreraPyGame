import pygame
import sys
import random

class Runner():
    __customs = ['turtle_2','turtle_2','turtle_2','turtle_2','turtle_2']
                     
    def __init__(self, x = 0, y = 0, custom=None):
        ixcustom = random.randint(0,4)
        self.custom = pygame.image.load('images/{}.png'.format(self.__customs[ixcustom])).convert()
        self.position = [x,y]
        self.name = ""

    def avanzar(self):
        self.position[0] += random.randint(1,5)
        

        

class Game():
    runners = []
    __startLine = 5  #porque no lleva self. antes de '___'?
    __finishLine = 620
    __posY = (160,200,240,280)
    __names = ('Speedy','Lucera', 'Alonso', 'Torcuata')
    
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.background = pygame.image.load('images/background_2.jpg').convert()

        for i in range(4):

            theRunner = Runner(self.__startLine, self.__posY[i])  #el self en esta línea es el 'Game' o el 'Runner'? (intuitivamente, el Game, no?)
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        #runners[i] = Runner(self.__startLine, self.__posY[i], __customs[i]) 
         
                
        pygame.display.set_caption("Carrera de bichos")

    def close(self):
        pygame.quit() #uninitialize all pygame modules 
        sys.exit()
        
    def competir(self):
        
        gameOver = False
        
        while not gameOver:
            #comprobación de eventos
            for event in pygame.event.get(): #devuelve un iterable con todos los eventos desde la última comprobación
                if event.type == pygame.QUIT:
                    gameOver = True 


            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    print('El corredor {} ha ganado'.format(runner.name))
                    gameOver = True
                    
            #dibujo del background
            self.__screen.blit(self.background,(0,0)) #en pygame el origen del plano (0,0) está en la esq. superior izq. de un cuadrante único.

            #dibujo de los cuatro corredores 
            for runner in self.runners:
                self.__screen.blit(runner.custom, runner.position)
                

            pygame.display.flip() #flip() refresca/muestra los objetos actualizados en la pantalla 

            pygame.time.delay(20)

        while True: #El bucle FOR de escucha de eventos debe ser anidado en un bucle WHILE infinito;
                    #de lo contrario acumulará todos los eventos hasta este punto hasta congelarse y
                    #no responder a la acción de quit
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()

        

if __name__ == '__main__':
    
    pygame.init()  #initialize all imported pygame modules
    game = Game()
    game.competir()
