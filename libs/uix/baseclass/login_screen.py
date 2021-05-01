import utils
from kivymd.uix.screen import MDScreen

utils.load_kv("login_screen.kv")


class LoginScreen(MDScreen):
	def __init__(self,**kwargs):
		super(LoginScreen, self).__init__()