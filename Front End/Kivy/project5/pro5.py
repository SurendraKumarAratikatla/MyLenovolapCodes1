from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from helpers5 import screen_help
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import BoxLayout

Window.size = (350, 600)


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class AllItemsScreen(Screen):
    pass

class RationScreen(Screen):
    pass


class BellScreen(Screen):
    pass

class FreshEggsScrren(Screen):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class AboutScreen(Screen):
    pass

class NotificationScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(AllItemsScreen(name='allitems'))
sm.add_widget(AllItemsScreen(name='ration'))
sm.add_widget(AllItemsScreen(name='eggs'))


class DemoApp(MDApp):
    class DrawerList(ThemableBehavior, MDList):
        pass
    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        firstpage = Builder.load_string(screen_help)
        screen.add_widget(firstpage)
        return screen

    def navigation_draw(self):
        sm = ScreenManager()
        sm.add_widget(AllItemsScreen(name='bell'))



DemoApp().run()
