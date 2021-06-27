from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from helphelpers import screen_help
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDTimePicker, MDThemePicker
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.slider import Slider
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior


import sqlite3 as sql
import re
from kivymd.uix.taptargetview import MDTapTargetView
from twilio.rest import Client
from twilio.twiml.voice_response import Record, VoiceResponse

Window.size = (350, 600)

class MenuScreen(Screen):
    pass

class UserLoginScreen(Screen):
    mobile: ObjectProperty()
    user: ObjectProperty()
    address: ObjectProperty()

    def get_started(self):
        print('here we go')

    def add_user(self):
        con = sql.connect('user.db')
        cur = con.cursor()
        cur.execute(""" INSERT INTO id (mobile,user,address) VALUES (?,?,?)""",
                    (self.mobile.text, self.user.text, self.address.text))
        con.commit()
        con.close()
        screen = Screen()
        mobile_no_string = self.mobile.text
        print(self.mobile.text)
        print(self.user.text)
        print(self.address.text)
        print(len(self.mobile.text))
        if re.match("^[0-9]\d{10}$", self.mobile.text):
            pass
        else:
            label = MDLabel(text='*You entered incorrect mobile number,', theme_text_color='Custom',
                            text_color=(0, 1, 0, 1), font_style='H6', pos_hint={'center_x': 0.5, 'center_y': 0.3})
            screen.add_widget(label)



#user classes

class UserShopItemsScreen(Screen):
    pass

class UserNonVegScreen(Screen):
    pass

class UserEggsScreen(Screen):
    shopname: ObjectProperty()
    eggrate: ObjectProperty()
    eggtrayrate: ObjectProperty()
    def add_user(self):
        con = sql.connect('user.db')
        cur = con.cursor()
        cur.execute(""" INSERT INTO eggs (shopname,eggrate,eggtrayrate) VALUES (?,?,?)""",
                    (self.shopname.text, self.eggrate.text, self.eggtrayrate.text))
        con.commit()
        con.close()
        screen = Screen()
        print(self.shopname.text)
        print(self.eggrate.text)
        print(self.eggtrayrate.text)
        if self.shopname.text and self.eggrate.text and self.eggtrayrate.text:
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
        if re.match("^[0-9]\d{10}$", self.mobile.text):
            print('correct mobile number')
        else:
            print('you entered incorrect mobile number')
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
    shopname: ObjectProperty()
    eggrate: ObjectProperty()
    eggtrayrate: ObjectProperty()

    data_items = ListProperty([])
    data_items1 = ListProperty([])

    def __init__(self, **kwargs):
        super(FreshEggsScrren, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        connection = sql.connect("user.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM eggs ORDER BY shopname ASC")
        rows = cursor.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)
        print("data items are")

        for item in self.data_items:
            if item != '':
                self.data_items1.append(item)
        print(self.data_items1)


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
sm.add_widget(UserLoginScreen(name='userlogin'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(AllItemsScreen(name='allitems'))
sm.add_widget(AllItemsScreen(name='ration'))
sm.add_widget(AllItemsScreen(name='eggs'))
sm.add_widget(AllItemsScreen(name='aboutration'))
sm.add_widget(UserShopItemsScreen(name='usershopitems'))
sm.add_widget(UserNonVegScreen(name='usernonveg'))
sm.add_widget(UserEggsScreen(name='usereggs'))




class DrawerList(ThemableBehavior, MDList):
    pass


class DemoApp(MDApp):
    shopname = ObjectProperty()
    eggrate = ObjectProperty()
    eggtrayrate = ObjectProperty()
    print("---------------------------->"+str(eggrate))
    data = {
        'phone': 'Tell Your Products',
        'pencil': 'Text Your Products',
        'microphone': 'Record Your Products',
    }

    def on_leave(self, instance):
        print('Exit from loop')

    def callback(self, instance):
        #print('yessssssss')
        print(instance.icon)

        # code for voice recording to make order

        if instance.icon == 'microphone':
            print('I am listening you please record and send your order...')




        # code for call to make order

        # if instance.icon == 'phone':
        #     account_sid = 'AC01b96e6ad4777b98b21ee5cd82b37365'
        #     auth_token = 'b82b160693c854b6ee542d23621e87c6'
        #
        #     client = Client(account_sid, auth_token)
        #
        #     call = client.calls.create(twiml='<Response><Say>Hello Surendra</Say></Response>', to='+918500906002',
        #                                from_='+12513255394')
        #
        #     print(call.sid)





    try:
        con = sql.connect('user.db')
        cur = con.cursor()
        cur.execute(""" CREATE TABLE id(
                mobile text,
                user text,
                address text)
                """)
        cur.execute(""" CREATE TABLE eggs(
                        shopname text,
                        eggrate text,
                        eggtrayrate text)
                        """)
        con.commit()
        con.close()
    except:
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

    def navigation_draw_1(self,instance):
        pass

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.open()


    # chip functions to choose store type to the customers

    def ration_store_chip(self,*args):
        print(args[1])

    def non_veg_chip(self,*args):
        print(args[1])

    def vegetables_chip(self,*args):
        print(args[1])

    def fruits_chip(self,*args):
        print(args[1])

    def sports_kits_chip(self,*args):
        print(args[1])

    def street_food_chip(self,*args):
        print(args[1])

    def others_chip(self,*args):
        print(args[1])

    # def tap_target_start(self):
    #     if self.tap_target_view.state == "close":
    #         self.tap_target_view.start()
    #     else:
    #         self.tap_target_view.stop()

if __name__ == '__main__':
    DemoApp().run()
