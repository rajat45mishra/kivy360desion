from kivymd.uix.screen import MDScreen
import utils
utils.load_kv("home_screen.kv")
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Point
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout  
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy import utils as colu
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.textfield import MDTextField
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    FakeRectangularElevationBehavior,
)
class RectangularElevationButton(
    RectangularRippleBehavior,
    FakeRectangularElevationBehavior,
    ButtonBehavior,
    Image,
    BackgroundColorBehavior,
    MDTooltip
):
    md_bg_color = [192,192,192, 1]
    icon = StringProperty("1.png")
class CustomDropDown(BoxLayout):
	text=StringProperty("Open Dropdown")
class CustDropDown(DropDown):
	def __init__(self,**kwargs):
		super(CustDropDown, self).__init__()
		self.dismiss()
class ThirdScreen(Image):
	rect_box = ObjectProperty(None)
	t_x = NumericProperty(0.0)
	t_y = NumericProperty(0.0)
	x1 = NumericProperty(0.0)
	y1 = NumericProperty(0.0)
	x2 = NumericProperty(0.0)
	y2 = NumericProperty(0.0)
	def enable_cropping(self):
		print ("pos///")
		print (self.pos)
		print("\nThirdScreen:")
		print(self.pos)
		print(self.size)
		print("\tAbsolute size=", self.ids.main_image.norm_image_size)
		print("\tAbsolute pos_x=", self.ids.main_image.center_x - self.ids.main_image.norm_image_size[0] / 2.)
		print("\tAbsolute pos_y=", self.ids.main_image.center_y - self.ids.main_image.norm_image_size[1] / 2.)
	def on_touch_down(self, touch):
		width, height = self.norm_image_size
		if self.center_x - width / 2 < touch.x < self.center_x + width / 2 and self.center_y - height / 2 < touch.y < self.center_y + height / 2:
			self.x1 = touch.x
			self.y1 = touch.y
			self.t_x = touch.x
			self.t_y = touch.y
		touch.grab(self)
		print(self.x1, self.y1)
		print("rectpos",self.x1, self.y1,(self.t_x - self.x1, self.t_y - self.y1) )
		print ("pos///up")
		print (self.pos,self.size)
	def on_touch_move(self, touch):
		width, height = self.norm_image_size
		if touch.grab_current is self:
			if self.center_x - width / 2 < touch.x < self.center_x + width / 2 and self.center_y - height / 2 < touch.y < self.center_y + height / 2:
				self.t_x = touch.x
				self.t_y = touch.y
			print(self.t_x, self.t_y)
			print("rectpos",self.x1, self.y1,(self.t_x - self.x1, self.t_y - self.y1) )
	def on_touch_up(self, touch):
		if touch.grab_current is self:
			self.x2 = touch.x
			self.y2 = touch.y
			print(self.x2, self.y2)
			print("pos///dow")
			print(self.pos,self.size)
			print("rectpos",self.x1, self.y1,(self.t_x - self.x1, self.t_y - self.y1) )
class AnotherScreen2(BoxLayout):
    def __init__(self, **kwargs):
        super(AnotherScreen2,self).__init__(**kwargs)
    def post(self):
        global pname
        pname=self.ids.klo.text
        global nop
        nop=self.ids.kl.text
        print(pname,nop)
class HomeScreen(MDScreen):
	dialog=None
	def show_simple_dialog(self):
		text=AnotherScreen2()
		Project_name=text.ids.klo.text
		photos=text.ids.kl.text
		print(Project_name,photos)
		if not self.dialog:
			self.dialog = Popup(
				title="Create Project:",
				size_hint=(.4,.4),
				background="/home/rajat/os/app/360/data/pop.png",
				title_color=colu.get_color_from_hex("#104E8B"),
                content=text,
                )
		self.dialog.open()