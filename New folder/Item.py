from connectionAssets import *
class Blue_carrot(pygame.sprite.Sprite):
	def __init__(self, X, Y):
		super().__init__()
		self.image = blue_carrot_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (X, Y)