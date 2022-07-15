import pygame as py
from pygame.locals import *
import os
py.init()

altura = 1000
largura = 1000
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal , 'img')
tela = py.display.set_mode((altura,largura))
py.display.set_caption('C-R (COUNTERUN)')

# define alguumas variaveis do jogo

bloco_tam = 200




#imagens
fundo_img = py.image.load(os.path.join(diretorio_imagens, 'sun.png')).convert_alpha()
bloco_img = py.image.load(os.path.join(diretorio_imagens, 'sky.png')).convert_alpha()

#bloco_img = py.transform.scale(bloco_img, (64,64))
#fundo_img =py.transform.scale(fundo_img, (1200,720))





def linhas_brancas():
	for linha in range(0,6):
		py.draw.line(tela, (255, 255, 255), (0, linha * bloco_tam), (largura, linha * bloco_tam))
		py.draw.line(tela, (255, 255, 255), (linha * bloco_tam, 0), (linha * bloco_tam, altura))
        #so pra eu me achar na lista


#mundo

class Mundo():
    def __init__(self,lista):
        self.bloco_lista = []

        #carregar imagens
        bloco_cima = py.image.load(os.path.join(diretorio_imagens, 'grass.png')).convert_alpha()
        bloco_em = py.image.load(os.path.join(diretorio_imagens, 'dirt.png')).convert_alpha()
        
        linha_cntor = 0
        for linha in lista:
            col_cntdor = 0
            for bloco in linha:
                if bloco == 1:
                    img = py.transform.scale(bloco_em , (bloco_tam,bloco_tam))
                    img_rect = img.get_rect()
                    img_rect.x = col_cntdor * bloco_tam
                    img_rect.y = linha_cntor * bloco_tam
                    bloco = (img, img_rect)
                    self.bloco_lista.append(bloco)

                if bloco == 2:
                    img = py.transform.scale(bloco_cima , (bloco_tam,bloco_tam))
                    img_rect = img.get_rect()
                    img_rect.x = col_cntdor * bloco_tam
                    img_rect.y = linha_cntor * bloco_tam
                    bloco = (img, img_rect)
                    self.bloco_lista.append(bloco)
                col_cntdor += 1
            linha_cntor += 1

    def desenhar(self):
        for bloco in self.bloco_lista:
            tela.blit(bloco[0], bloco[1])

mapa_lista =[
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 2, 2, 2, 1]
]

mundo = Mundo(mapa_lista)
rodar= True

while rodar:
    
    #print(mundo.lista_obj)
    
    tela.blit(fundo_img, (0,0))
    tela.blit(bloco_img, (100,100))

    mundo.desenhar()
    linhas_brancas()
    for event in py.event.get():
        if event.type == py.QUIT:
            rodar = False

    py.display.update()
py.quit()