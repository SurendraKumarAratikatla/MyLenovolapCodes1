from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


KV = '''
<ListItemWithCheckbox>:

    IconLeftWidget:
        icon: root.icon

    RightCheckbox:


BoxLayout:

    ScrollView:

        MDList:
            id: scroll
'''


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        l = ['తెలుగు','పెసరపప్పు','మినపప్పు','సెనగపప్పు']
        icons = ['plus','language-python','shopping','face']

        for i in l:
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=i, icon=icons[3])

            )


MainApp().run()