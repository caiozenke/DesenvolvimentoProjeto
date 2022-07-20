
import pygame as py
from pygame.locals import *

py.init()

#Variaveis Do Jogo
largura = 1700
altura = 1000
tela = py.display.set_mode((largura, altura))
py.display.set_caption('crias')
clock = py.time.Clock()
fps = 60
bloco_tam = 50



#Carregando Imagens do Fundo e Transformando a escala de um
sol_img = py.image.load('img/sol.png')
ceu_img = py.image.load('img/ceu_fundo.jpg')
ceu_img = py.transform.scale(ceu_img, (1700 , 1000))



#Metodo desenha linhas Brancas na Tela, Ajuda a Montar a Lista
def desenhar_branco():
	for linha in range(0, 35):
		py.draw.line(tela, (255, 255, 255), (0, linha * bloco_tam), (largura, linha * bloco_tam))
		py.draw.line(tela, (255, 255, 255), (linha * bloco_tam, 0), (linha * bloco_tam, altura))



class Personagem():
    
	def __init__(self, x,y):
     
		"""Passando as Imagens da Direita na Variavel img_direita e lhe a adicionando na Lista vazia 
  		e fazendo a mesma coisa com img_esquerda, apenas utilizando a função flip dentro do loop for"""
    
		self.imagens_direita = []
		self.imagens_esquerada = []
		self.index = 0
		self.cntdr_lista = 0
		
		for num in range(1,5):
			img_direita = py.image.load(f'img/teste{num}.png')
			img_direita = py.transform.scale(img_direita, (40,80))
			img_esquerda =py.transform.flip(img_direita,True,False)
			self.imagens_direita.append(img_direita)
			self.imagens_esquerada.append(img_esquerda)   			
		
  
		#Personagem Variaveis
		self.image = self.imagens_direita[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.largura = self.image.get_width()
		self.altura = self.image.get_height()
		self.vel_y= 0
		self.pulo = False
		self.direcao = 0
	

	

	def update(self):
		#Atualização Do Personagem na Tela
		delta_x= 0
		delta_y = 0
		moviment_tempo = 5
  
		tecla = py.key.get_pressed()
  
  
		#Movimentação
  
		"""Coordena o Pulo do Personagem, impossibilitando dele ficar pulando em sequencialmente ate sair da tela com a variavel self.pulo sendo um Bool
  			e a movimentação padrao do Personagem"""
     
		if tecla[py.K_SPACE] and self.pulo == False:
			self.vel_y = -15
			self.pulo = True
		if tecla[py.K_SPACE] == False:
			self.pulo = False
   
		if tecla[py.K_a]:
			delta_x -= 5
			self.cntdr_lista +=1
			self.direcao = -1
		if tecla[py.K_d]:
			delta_x += 5
			self.cntdr_lista +=1
			self.direcao = 1
   
		if tecla[py.K_d] == False and tecla[py.K_a] == False:
			self.cntdr_lista = 0
			self.index = 0
			if self.direcao == 1:
				self.image = self.imagens_direita[self.index]
			if self.direcao == -1:
				self.image = self.imagens_esquerada[self.index]

  
		#Adicionando Gravidade
  
		"""A cada Literação(execução) nao quero ficar subindo infinitamente, entao defino y como um positivo para
  			ficar puxando o personagem para baixo"""
		
		self.vel_y += 1
		if self.vel_y >10:
			self.vel_y = 10
		delta_y += self.vel_y

		#Colisão
  
		"""Uso a função colliderect apenas passando as variaveis que ela pede e alterando o rect.x na colisão horizontal e rect.y na vertical"""
  
		for bloco in mundo.bloco_lista:
			#direcão x colisão
			if bloco[1].colliderect(self.rect.x + delta_x, self.rect.y, self.largura, self.altura):
				delta_x = 0

    
    		#direção y cxolisao
			if bloco[1].colliderect(self.rect.x, self.rect.y + delta_y,self.largura,self.altura):
				
				#Para o personagem bater no bloco de cima e descer
				if self.vel_y < 0:
					delta_y = bloco[1].bottom - self.rect.top
					self.vel_y = 0
				elif self.vel_y >= 0:
					delta_y = bloco[1].top - self.rect.bottom					
					self.vel_y = 0

		#Animação
		"""Percorrendo a Lista da imagens e definindo um tempo para animações nao ficaram corridas , quando direção for positiva 
  		o index percorrerar a lista de imagens da direita , quando negativa irá para esquerda e zerando ele qunado nao houver toque  """		
		if self.cntdr_lista > moviment_tempo:
			self.cntdr_lista = 0
			self.index +=1
			if self.index >= len(self.imagens_direita):
				self.index = 0
			if self.direcao == 1:
				self.image = self.imagens_direita[self.index]
			if self.direcao == -1:
				self.image = self.imagens_esquerada[self.index]
	
  
		"""Definindo as Novas Posições do Personagem e Blitando Ele"""
		self.rect.x += delta_x
		self.rect.y += delta_y
		tela.blit(self.image , self.rect)
		
	

class Mundo():
	def __init__(self, lista):
		self.bloco_lista = []

		#carregando imagens dos blocos 
		terra_img = py.image.load('img/terra.png')
		terreno_img = py.image.load('img/terreno2.png')
  
  
		"""Este método percorre a lista adicionando nela onde for tal variavel 
  		a imagem que estou adicionando na self.bloco_lista  """

		linha_cntdr = 0
		for linha in lista:
			coluna_cntdr = 0
			for bloco in linha:
				if bloco == 1:
					img = py.transform.scale(terra_img, (bloco_tam, bloco_tam))
					img_rect = img.get_rect()
					img_rect.x = coluna_cntdr * bloco_tam
					img_rect.y = linha_cntdr * bloco_tam
					bloco = (img, img_rect)
					self.bloco_lista.append(bloco)
				if bloco == 2:
					img = py.transform.scale(terreno_img, (bloco_tam, bloco_tam))
					img_rect = img.get_rect()
					img_rect.x = coluna_cntdr * bloco_tam
					img_rect.y = linha_cntdr * bloco_tam
					bloco = (img, img_rect)
					self.bloco_lista.append(bloco)
			
				coluna_cntdr += 1
			linha_cntdr += 1

	def desenhar(self):
		#percorre a lista e desenha ela na tela
		for bloco in self.bloco_lista:
			tela.blit(bloco[0], bloco[1])
			#py.draw.rect(tela, (255,255,255),bloco[1], 2)




#Lista do Mapa
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
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 , 2, 2, 2, 2, 2, 2 , 2, 2, 2, 2, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1]
]


#Instancias das classe
perso= Personagem(100 , altura - 130)
mundo = Mundo(mapa_lista)



rodar = True
while rodar:
	clock.tick(60)
	tela.blit(ceu_img, (0, 0))
	tela.blit(sol_img, (100, 100))

	mundo.desenhar()
	perso.update()
	#desenhar_branco()

	for event in py.event.get():
		if event.type == py.QUIT:
			rodar = False

	py.display.update()

py.quit()