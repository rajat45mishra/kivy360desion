import utils
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivy.uix.button import Button

utils.load_kv("ImagesPl.kv")


class ImagesPl(MDScreen):
	dob=None
	def __init__(self,**kwargs):
		super(ImagesPl, self).__init__()
class ButtonILike(Button):
    pass