# for i in range(10):
# 	print("guts is ok %d" % i)
# print("good bye")
import time
import pygame


class Dog:
	def __init__(self, state):
		self.x = 0
		self.y = 0
		self.state = state
		self.hungry_when = 200
		self.rip = 2000
		self.dead = False

	def speak(self):
		print(self.x)
		print(self.y)
		print(self.state)
		print(self.hungry_when)

	def feed(self):
		self.hungry_when += 300
		self.rip += 1000

def main():
	pygame.init()
	happy  = pygame.transform.scale(pygame.image.load("happy_dogge.png"), (600, 1200))
	hungry = pygame.transform.scale(pygame.image.load("hungry_dogge.png"), (600, 1200))
	dead   = pygame.transform.scale(pygame.image.load("RIP.png"), (600, 1200))
	screen = pygame.display.set_mode((600, 600))

	dog = Dog(happy)
	dog.speak()

	running = True
	counter = 0
	previous_mouse = (0, 0, 0)
	while running == True: 
		
		counter +=1

		# Input
		mouse = pygame.mouse.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:	
				running = False

		if counter % 20 == 0:
			dog.y -= 600
			if dog.y == -1200:
				dog.y = 0

		if dog.dead == False:
			if mouse[0] == 1 and previous_mouse[0] == 0:
				dog.feed()
				dog.state = happy

			if counter % dog.hungry_when == 0:
				dog.state = hungry

			if counter == dog.rip:
				dog.state = dead
				dog.dead = True

		# Output
		screen.fill((255, 255, 255))
		screen.blit(dog.state, (dog.x, dog.y))
		pygame.display.flip()	
		time.sleep(0.01)

		previous_mouse = mouse

main()
