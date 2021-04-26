import utils
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivy.uix.button import Button
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout

utils.load_kv("subfolder.kv")
class SubFolder(MDScreen):
	def __init__(self,**kwargs):
		super(SubFolder, self).__init__()