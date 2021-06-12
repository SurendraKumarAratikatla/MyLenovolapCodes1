from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder


Window.size = (400, 600)

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'VZM'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: ''
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'


"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))

class FreshEggsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        #screen = Screen()
        screen = Builder.load_string(screen_helper)
        #icon_btn = MDFloatingActionButton(icon='egg', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #screen.add_widget(icon_btn)

        return screen

FreshEggsApp().run()