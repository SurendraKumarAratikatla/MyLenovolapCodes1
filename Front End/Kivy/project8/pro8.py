from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from helpers8 import screen_help
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
from kivymd.uix.taptargetview import MDTapTargetView


KV = '''
Screen:

    MDFloatingActionButton:
        id: button
        icon: "head-question"
        pos: 10, 10
        on_release: app.tap_target_start()
        elevation_normal: 10
'''



Window.size = (350, 600)

class MenuScreen(Screen):
    pass

class UserCustomerScreen(Screen):
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
        cur.execute(""" INSERT INTO id (mobile,user,address) VALUES (?,?,?)""", (self.mobile.text, self.user.text, self.address.text))
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

class AboutRationScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AllItemsScreen(name='usercustomer'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(AllItemsScreen(name='allitems'))
sm.add_widget(AllItemsScreen(name='ration'))
sm.add_widget(AllItemsScreen(name='eggs'))
sm.add_widget(AllItemsScreen(name='aboutration'))

class DrawerList(ThemableBehavior, MDList):
    pass


class DemoApp(MDApp):
    data = {
        'basket': 'Today Offers',
        'offer': 'Discounts',
        'cart': 'Cart Page',
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
        #screen = Screen()
        firstpage = Builder.load_string(screen_help)

        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text="VZM Store",
            description_text='''Anyone can login as a user and
you can publish your products to customers''',
            widget_position="left_bottom",
            target_circle_color=(142/255.0, 172/255.0, 249/255.0),
        )

        screen.add_widget(firstpage)

        return screen

    def navigation_draw(self):
        sm = ScreenManager()
        sm.add_widget(AllItemsScreen(name='bell'))

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

if __name__ == '__main__':
    DemoApp().run()
