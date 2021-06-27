screen_help ="""
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget


<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<MyBackdropFrontLayer@ItemBackdropFrontLayer>
    backdrop: None
    text: "Find amma home made food"
    secondary_text: "near by you"
    icon: "transfer-down"
    pos_hint: {"top": 1}
    _no_ripple_effect: True


<MyBackdropBackLayer@Image>
    size_hint: 1, 1
    source: "foodimg4.png"
    pos_hint: {"center_x": .4, "center_y": .5}

<AmmaFood>

    MDBackdrop:
        id: backdrop
        left_action_items: [['menu', lambda x: self.open(open_up_to=0)]]
        title: "Amma Food"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Menu"
        padding:  [1, 0, 1, 0]
        back_layer_color: rgba('#0e1574ff')
        front_layer_color: rgba('#0e1574ff')
        
        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
"""