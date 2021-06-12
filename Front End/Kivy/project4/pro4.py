from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from helpers import screen_help
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.theming import ThemableBehavior



Window.size = (350, 600)

class MenuScreen(Screen):
    pass


class ProfileScreen(MDTextField):
    def __int__(self):
        return print('mobile number is:'+str(id))


class AllItemsScreen(Screen):
    pass

class RationScreen(Screen):
    pass


class BellScreen(Screen):
    pass

class FreshEggsScrren(Screen):
    def increment_value(self,**kwargs):
        print('in function')

class NotificationScreen(Screen):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class AboutScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(AllItemsScreen(name='allitems'))
sm.add_widget(AllItemsScreen(name='ration'))
sm.add_widget(AllItemsScreen(name='eggs'))
sm.add_widget(AllItemsScreen(name='bell'))
sm.add_widget(AllItemsScreen(name='notification'))
sm.add_widget(AllItemsScreen(name='about'))

class DemoApp(MDApp):
    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        self.firstpage = Builder.load_string(screen_help)
        screen.add_widget(self.firstpage)
        return screen

    def about_draw(self):
        #sm = ScreenManager()
        #sm.add_widget(AllItemsScreen(name='bell'))
        print('about')

    def on_start(self):
        pass

    def navigation_draw(self):
        print('navigation')

DemoApp().run()
