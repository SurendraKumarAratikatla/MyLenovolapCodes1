from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
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




# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))



class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()