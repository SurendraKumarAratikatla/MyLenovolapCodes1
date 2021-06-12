from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField


class FreshEggsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        label = MDLabel(text='Click Me', halign='center', theme_text_color='Custom',
                        text_color=(0, 1, 0, 1), font_style='H6')

        icon = MDIcon(icon='language-python', halign='center')

        btn_flat = MDRectangleFlatButton(text='Submit', pos_hint={'center_x': 0.5, 'center_y': 0.1})
        icon_btn = MDFloatingActionButton(icon='egg', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(icon_btn)

        return screen


FreshEggsApp().run()
