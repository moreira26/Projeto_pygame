import pygame
pygame.init()

x = 400      #posição da bolinha
y = 300      #posição da bolinha
velocidade = 100

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("criando game")#nome na janela do jogo

janela_abrir = True #jogo rodando

while janela_abrir:
    pygame.time.delay(50)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #botão de fechamento do jogo
            janela_abrir = False
            
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_w]:
            y-= velocidade
        
        if comandos[pygame.K_s]:
            y+= velocidade
        
        if comandos[pygame.K_d]:
            x-= velocidade
        
        if comandos[pygame.K_a]:
            x+= velocidade
        
    janela.fill((0,0,0))        
    pygame.draw.circle(janela, (0,255,0), (400,300),50)      #criação de um circulo            
    pygame.display.update()            
            
pygame.quit()
