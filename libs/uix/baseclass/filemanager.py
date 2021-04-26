import utils
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivy.uix.button import Button
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
utils.load_kv("filemanager.kv")
class FileManager(MDScreen):
	def __init__(self,**kwargs):
		super(FileManager, self).__init__()
class ButtonILike(Button):
    pass
class CustomOneLineIconListItem2(GridLayout):
	icon = StringProperty()
	text= StringProperty()
	def printS(self,data):
		print(data)
	
class CustomOneLineIconListItem(MDCard,ButtonBehavior):
	icon = StringProperty()
	text= StringProperty()
	def printS(self,data):
		print(data)
class PreviousMDIcons(MDScreen):
	app=App.get_running_app()
	def set_list_md_icons(self, text="", search=False):
		def add_icon_item(name_icon):
			self.ids.rv.data.append(
				{
				"viewclass": "CustomOneLineIconListItem2",
				"icon": name_icon,
				"text": name_icon,
				"callback": lambda x:app.root.change_screen("subfolder") ,
				}
			)
		self.ids.rv.data = []
		for name_icon in md_icons.keys():
			if search:
				if text in name_icon:
					add_icon_item(name_icon)
			else:
				add_icon_item(name_icon)