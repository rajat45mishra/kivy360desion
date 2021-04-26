import utils
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivy.uix.button import Button

utils.load_kv("signup_screen.kv")


class SignupScreen(MDScreen):
	dob=None
	def __init__(self,**kwargs):
		super(SignupScreen, self).__init__()
class ButtonILike(Button):
    pass