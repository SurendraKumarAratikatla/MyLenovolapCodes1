from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from helpers import username_helper,address_helper,mobileno_helper,screen_helper,screen_help
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window


Window.size = (400, 600)

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        label = MDLabel(text='Please enter the following details', font_style='H6',pos_hint = {'center_x':0.6,'center_y':0.8})
        #self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        #username = MDTextField(text = 'Enter username', pos_hint = {'center_x':0.5,'center_y':0.5}, size_hint = (0.5,1))

        mobile = Builder.load_string(mobileno_helper)
        username = Builder.load_string(username_helper)
        address = Builder.load_string(address_helper)
        header = Builder.load_string(screen_helper)
        button = MDRectangleFlatButton(text = 'Submit', pos_hint = {'center_x':0.5,'center_y':0.2})
        screen.add_widget(mobile)
        screen.add_widget(username)
        screen.add_widget(address)
        screen.add_widget(button)
        screen.add_widget(header)
        screen.add_widget(label)
        print('i am entered into this loop')
        return screen






# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))



class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Please enter the following details', font_style='H6',
                        pos_hint={'center_x': 0.6, 'center_y': 0.8})
        screen = Screen()
        mobile = Builder.load_string(mobileno_helper)
        username = Builder.load_string(username_helper)
        address = Builder.load_string(address_helper)
        header = Builder.load_string(screen_helper)
        button = MDRectangleFlatButton(text='Submit', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        screen.add_widget(mobile)
        screen.add_widget(username)
        screen.add_widget(address)
        screen.add_widget(button)
        screen.add_widget(header)
        screen.add_widget(label)

        return screen
    def navigation_draw(self):
        print("navigation")

DemoApp().run()