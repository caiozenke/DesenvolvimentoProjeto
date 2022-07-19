import pygame as py
from pygame.locals import *

py.init()

largura = 1700
altura = 1000

tela = py.display.set_mode((largura, altura))
py.display.set_caption('crias')

#define game variables
bloco_tam = 50


#load images
sol_img = py.image.load('img/sun.png')
ceu_img = py.image.load('img/sky.jpg')
ceu_img = py.transform.scale(ceu_img, (1700 , 1000))
def desenhar_branco():
	for linha in range(0, 35):
		py.draw.line(tela, (255, 255, 255), (0, linha * bloco_tam), (largura, linha * bloco_tam))
		py.draw.line(tela, (255, 255, 255), (linha * bloco_tam, 0), (linha * bloco_tam, altura))

class Personagem():
	def __init__(self, x,y):
		img = py.image.load('img/guy1.png')
		self.image = py.transform.scale(img, (40,80))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	

	

	def update(self):
		delta_x= 0
		delta_y = 0
		tecla = py.key.get_pressed()

		if tecla[py.K_a]:
			delta_x -= 5
		if tecla[py.K_d]:
			delta_x += 5


		self.rect.x += delta_x
		self.rect.y += delta_y
		tela.blit(self.image , self.rect)
	

class Mundo():
	def __init__(self, data):
		self.bloco_lista = []

		#load images
		dirt_img = py.image.load('img/dirt.png')
		grass_img = py.image.load('img/terreno2.png')

		linha_cntdr = 0
		for linha in data:
			coluna_cntdr = 0
			for bloco in linha:
				if bloco == 1:
					img = py.transform.scale(dirt_img, (bloco_tam, bloco_tam))
					img_rect = img.get_rect()
					img_rect.x = coluna_cntdr * bloco_tam
					img_rect.y = linha_cntdr * bloco_tam
					bloco = (img, img_rect)
					self.bloco_lista.append(bloco)
				if bloco == 2:
					img = py.transform.scale(grass_img, (bloco_tam, bloco_tam))
					img_rect = img.get_rect()
					img_rect.x = coluna_cntdr * bloco_tam
					img_rect.y = linha_cntdr * bloco_tam
					bloco = (img, img_rect)
					self.bloco_lista.append(bloco)
				coluna_cntdr += 1
			linha_cntdr += 1

	def draw(self):
		for bloco in self.bloco_lista:
			tela.blit(bloco[0], bloco[1])



mapa_lista = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 , 2, 2, 2, 2, 2, 2 , 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1]
]



perso= Personagem(100 , altura - 130)
mundo = Mundo(mapa_lista)

run = True
while run:

	tela.blit(ceu_img, (0, 0))
	tela.blit(sol_img, (100, 100))

	mundo.draw()
	perso.update()
	#desenhar_branco()

	for event in py.event.get():
		if event.type == py.QUIT:
			run = False

	py.display.update()

py.quit()