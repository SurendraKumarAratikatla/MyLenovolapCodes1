mobileno_helper = """
MDTextField:
    foreground_color : [0,0,1,1]
    hint_text : "Enter Mobile Number"
    helper_text_mode : "on_focus"
    icon_right : "cellphone-android"
    icon_right_color : app.theme_cls.primary_color
    pos_hint : {'center_x':0.5, 'center_y': 0.6}
    text_color: (0,1,0)
    size_hint_x : None
    width : 300
"""

username_helper = """
MDTextField:
    hint_text : "Enter username"
    helper_text_mode : "on_focus"
    icon_right : "account"
    icon_right_color : app.theme_cls.primary_color
    pos_hint : {'center_x':0.5, 'center_y': 0.5}
    size_hint_x : None
    width : 300
"""

address_helper = """
MDTextField:
    hint_text : "Enter Address"
    helper_text_mode : "on_focus"
    icon_right : "home"
    icon_right_color : app.theme_cls.primary_color
    pos_hint : {'center_x':0.5, 'center_y': 0.4}
    size_hint_x : None
    width : 300
"""

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Eggs'
            left_action_items : [["menu",lambda x: app.navigation_draw()]]
            right_action_items : [["egg-easter",lambda x: app.navigation_draw()]]
            elevation : 10
        MDLabel:
            title : ''
"""
