from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon
from helpers import username_helper, address_helper, mobileno_helper, screen_helper
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window

Window.size = (400, 600)


class FreshEggsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        icon_btn = MDFloatingActionButton(icon='egg', pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          on_release=self.show_data)
        screen.add_widget(icon_btn)

        return screen

    def show_data(self, obj):
        self.theme_cls.primary_palette = "Blue"
        self.label = MDLabel(text='Please enter the following details', font_style='H6',
                             pos_hint={'center_x': 0.6, 'center_y': 0.8})
        # self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        # username = MDTextField(text = 'Enter username', pos_hint = {'center_x':0.5,'center_y':0.5}, size_hint = (0.5,1))

        self.mobile = Builder.load_string(mobileno_helper)
        self.username = Builder.load_string(username_helper)
        self.address = Builder.load_string(address_helper)
        self.header = Builder.load_string(screen_helper)
        self.button = MDRectangleFlatButton(text='Submit', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        screen.add_widget(self.mobile)
        screen.add_widget(self.username)
        screen.add_widget(self.address)
        screen.add_widget(self.header)
        screen.add_widget(self.button)
        screen.add_widget(self.label)
        print('entered into loop')
    def navigation_draw(self):
        print("navigation")


FreshEggsApp().run()
