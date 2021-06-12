from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp


Window.size = (400, 600)

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Python Top Interview Questions'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
        #on_release: self.show_data
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'hello i am here'
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
        #self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Blue"
        #screen = Screen()
        screen = Builder.load_string(screen_helper)
        #icon_btn = MDFloatingActionButton(icon='egg', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #screen.add_widget(icon_btn)
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        for i in range(100):
            btn = Button(text=str(i), size_hint_y=None, height=400)
            self.layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(self.layout)
        runTouchApp(root)

        return screen

FreshEggsApp().run()
print('ended')