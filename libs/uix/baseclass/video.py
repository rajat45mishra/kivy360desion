import utils
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivy.uix.button import Button

utils.load_kv("video.kv")


class VideoPl(MDScreen):
	dob=None
	def __init__(self,**kwargs):
		super(VideoPl, self).__init__()
class ButtonILike(Button):
    pass