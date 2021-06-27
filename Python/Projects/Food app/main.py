from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory

Window.size = (350, 600)

# Your layouts.
Builder.load_string(
    """
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget


<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<ItemBackdropBackLayer>
    size_hint_y: None
    height: self.minimum_height
    spacing: "10dp"

    canvas:
        Color:
            rgba:
                root.theme_cls.primary_dark if root.selected_item \
                else root.theme_cls.primary_color
        RoundedRectangle:
            pos: self.pos
            size: self.size

    MDIconButton:
        icon: root.icon
        theme_text_color: "Custom"
        text_color: 1, 1, 1, .5 

    MDLabel:
        text: root.text
        color: 1, 1, 1, .5 


<ItemBackdropBackLayerOfSecondScreen@BoxLayout>
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        size_hint: None, None
        size: "30dp", "30dp"
        active: False or self.active
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<ItemRoundBackdropBackLayerOfSecondScreen@BoxLayout>
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        group: "size"
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<MyBackdropFrontLayer@ScrollView>
    backdrop: None
    backlayer: None

    GridLayout:
        size_hint_y: None
        height: self.minimum_height
        cols: 1
        padding: "5dp"

        ItemBackdropFrontLayer:
            text: "Press item"
            secondary_text: "to Back"
            icon: "arrange-send-backward"
            on_press:
                root.backlayer.current = "one screen"
                root.backdrop.open()
                
        ItemBackdropFrontLayer:
            text: "Press item"
            secondary_text: "to Back"
            icon: "arrange-send-backward"
            on_press:
                root.backlayer.current = "two screen"
                root.backdrop.open()

        ItemBackdropFrontLayer:
            text: "Lower the front layer"
            secondary_text: " by 50 %"
            icon: "transfer-down"
            on_press:
                root.backdrop.open(-Window.height / 2)


<MyBackdropBackLayer@ScreenManager>
    transition: NoTransition()

    Screen:
        name: "one screen"
        MDScreen:
            MDRoundFlatIconButton:
                icon:"food"
                text: "Login"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 0, 1
                pos_hint: {"center_x": .5, "center_y": .5}
    
    Screen:
        name: "two screen"
        MDScreen:
            MDRectangleFlatButton:
                text: "MDRECTANGLEFLATBUTTON"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 1, 1
                pos_hint: {"center_x": .5, "center_y": .5}
        

    
"""
)

# Usage example of MDBackdrop.
Builder.load_string(
    """
<ExampleBackdrop>

    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [["menu", lambda x: self.open()]]
        title: "Amma Food"
        header_text: "Menu:"
        
        MDRoundFlatIconButton:
            icon:"food"
            text: "Logout"
            theme_text_color: "Custom"
            text_color: 1, 0, 0, 1
            line_color: 0, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .5}

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
"""
)


class ExampleBackdrop(Screen):
    pass


class ItemBackdropBackLayer(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        #self.title = "Amma Food"
        self.theme_cls.primary_palette = "Purple"
        super().__init__(**kwargs)

    def build(self):
        self.root = ExampleBackdrop()


if __name__ == "__main__":
    MainApp().run()
