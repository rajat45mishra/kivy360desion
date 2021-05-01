import utils
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.uix.tooltip import MDTooltip
from kivy.graphics import *
from kivy.properties import ObjectProperty
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    FakeRectangularElevationBehavior,
)
utils.load_kv("ImagesPl.kv")
class MyButton(ToggleButtonBehavior,Image,BackgroundColorBehavior,
    FakeRectangularElevationBehavior):
	md_bg_color = [192,192,192, 1]
	def __init__(self, **kwargs):
		super(MyButton, self).__init__(**kwargs)
		self.source = '1.png'
		self.elevation=12
	def on_state(self, widget, value):
		if value == 'down':
			self.source = '1.png'
			with self.canvas:
				Color(0,128,0)
				Line(width=3, rectangle=(self.x, self.y, self.width, self.height))
		else:
			self.source = '1.png'
			with self.canvas:
				Color(192,192,192)
				Line(width=3, rectangle=(self.x, self.y, self.width, self.height))
class ImagesPl(MDScreen):
	dob=None
	layout_content=ObjectProperty(None)
	def __init__(self,**kwargs):
		super(ImagesPl, self).__init__()
		if self.layout_content:
			self.layout_content.bind(minimum_height=self.layout_content.setter('height'))
class ButtonILike(Button):
    pass