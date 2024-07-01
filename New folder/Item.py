from connectionAssets import *
import  connectionAssets
class Item(pygame.sprite.Sprite):
	def __init__(self, X, Y, img):
		super().__init__()
		self.image = img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (X, Y)

