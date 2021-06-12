from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from helpers7 import screen_help
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import sqlite3 as sql
import re



Window.size = (350, 600)


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    mobile: ObjectProperty()
    user: ObjectProperty()
    address: ObjectProperty()

    def get_started(self):
        print('here we go')

    def add_user(self):
        con = sql.connect('user.db')
        cur = con.cursor()
        cur.execute(""" INSERT INTO id (mobile,user,address) VALUES (?,?,?)""", (self.mobile.text, self.user.text, self.address.text)
                    )
        con.commit()
        con.close()
        screen = Screen()
        mobile_no_string = self.mobile.text
        print(self.mobile.text)
        print(self.user.text)
        print(self.address.text)
        print(len(self.mobile.text))
        if re.match("^[0-9]\d{10}$", self.mobile.text) == None:
            pass
        else:
            label = MDLabel(text='*You entered incorrect mobile number,', theme_text_color='Custom',
                            text_color=(0, 1, 0, 1), font_style='H6', pos_hint={'center_x': 0.5, 'center_y': 0.3})
            screen.add_widget(label)

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


class DrawerList(ThemableBehavior, MDList):
    pass


class DemoApp(MDApp):
    data = {
        'history': 'About',

    }
    try:
        con = sql.connect('user.db')
        cur = con.cursor()
        cur.execute(""" CREATE TABLE id(
                mobile text,
                user text,
                address text)
                """)
        con.commit()
        con.close()
    except:
        pass

    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        #super().add_user(self)
        screen = Screen()
        firstpage = Builder.load_string(screen_help)
        screen.add_widget(firstpage)
        return screen

    def navigation_draw(self):
        sm = ScreenManager()
        sm.add_widget(AllItemsScreen(name='bell'))


if __name__ == '__main__':
    DemoApp().run()
