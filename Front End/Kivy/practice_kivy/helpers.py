screen_help = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    AllItemsScreen:
    RationScreen:
    BellScreen:
    #PropertyScreen:
    #DailyLaborScreen:
   #LocalJobs:
    FreshEggsScrren:
<MenuScreen>:
    name: 'menu'
    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
    MDFloatingActionButton:
        icon: "shopping"
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
        elevation_normal: 10
        #on_release: self.ProfileScreen

<ProfileScreen>:
    name: 'profile'
    MDTextField:
        foreground_color : [0,0,1,1]
        hint_text : "Enter Mobile Number"
        #required: True
        max_text_length : 10
        helper_text_mode : "on_focus"
        icon_right : "cellphone-android"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y': 0.6}
        text_color: (0,1,0)
        size_hint_x : None
        width : 300
    MDTextField:
        hint_text : "Enter username"
        max_text_length : 30
        #required: True
        helper_text_mode: "on_error"
        helper_text_mode : "on_focus"
        icon_right : "account"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y': 0.5}
        size_hint_x : None
        width : 300
    MDTextField:
        #multiline: True
        hint_text : "Enter Address"
        #required: True
        max_text_length : 100
        helper_text_mode : "on_focus"
        icon_right : "home"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y': 0.4}
        size_hint_x : None
        width : 300
    MDRectangleFlatButton:
        text : 'Submit'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        elevation_normal: 9
        on_press: root.manager.current = 'allitems'
        #on_release: self.AllItemsScreen
    MDLabel:
        text: 'Please enter the following details'
        font_style: 'H6'
        pos_hint: {'center_x':0.6,'center_y':0.8}
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'VZM Store'
                left_action_items : [["menu",lambda x: app.navigation_draw()]]
                right_action_items : [["shopping-search",lambda x: app.navigation_draw()]]
                elevation : 10
            MDLabel:
                title : ''

<AllItemsScreen>:
    name: 'allitems'
    ScrollView:
        MDList:
            OneLineAvatarIconListItem:
                text : ''
                IconLeftWidget:
                    icon: ""
            OneLineAvatarIconListItem:
                text : 'Ration-Store'
                on_press: root.manager.current = 'ration'
                elevation_normal: 10
                #on_release: self.RationScreen
                IconLeftWidget:
                    icon: "basket-fill"
            OneLineAvatarIconListItem:
                text : 'Property'
                IconLeftWidget:
                    icon: "home-city"
            OneLineAvatarIconListItem:
                text : 'Daily Labor Workers'
                IconLeftWidget:
                    icon: "nature-people"
            OneLineAvatarIconListItem:
                text : 'Local Jobs'
                IconLeftWidget:
                    icon: "email-search"
    
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Your Store'
                left_action_items : [["menu",lambda x: app.navigation_draw()]]
                right_action_items : [["bell",lambda x: app.navigation_draw()]]
                #on_press: root.manager.current = 'bell'
                elevation : 10
            MDLabel:
                title : ''
                
<RationScreen>:
    name: 'ration'
    ScrollView:
        MDList:
            OneLineAvatarIconListItem:
                text : ''
                IconLeftWidget:
                    icon: ""
            OneLineAvatarIconListItem:
                text : 'Daily-Ration'
                IconLeftWidget:
                    icon: "launch"
            OneLineAvatarIconListItem:
                text : 'Vegetables'
                IconLeftWidget:
                    icon: "leaf"
            OneLineAvatarIconListItem:
                text : 'Fresh-Eggs'
                on_press: root.manager.current = 'eggs'
                IconLeftWidget:
                    icon: "egg"
            OneLineAvatarIconListItem:
                text : 'Non-VegItems'
                IconLeftWidget:
                    icon: "egg-easter"
            OneLineAvatarIconListItem:
                text : 'Fruits'
                IconLeftWidget:
                    icon: "fruit-cherries"
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Your Store'
                left_action_items : [["menu",lambda x: app.navigation_draw()]]
                right_action_items : [["bell",lambda x: app.navigation_draw()]]
                elevation : 10
            MDLabel:
                title : ''
<BellScreen>:
    name: 'bell'
    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
    MDFloatingActionButton:
        icon: "bell"
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
        elevation_normal: 10
        on_release: self.ProfileScreen
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'All Notifications'
                elevation : 10
            MDLabel:
                title : ''
<FreshEggsScrren>:
    name: 'eggs'
    # MDScreen:
    #     radius: [25, 0, 0, 0]
    #     md_bg_color: app.theme_cls.primary_color
    MDFillRoundFlatIconButton:
        text: "Tray"
        icon: "egg-easter"
        pos_hint: {'center_x':0.5,'center_y':0.7}
        #on_press: root.manager.current = 'profile'
        elevation_normal: 12
        #on_release: self.ProfileScreen
    MDFillRoundFlatIconButton:
        text: "Individual"
        icon: "egg"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        #on_press: root.manager.current = 'profile'
        elevation_normal: 12
        #on_release: self.ProfileScreen
        
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Your Store'
                left_action_items : [["menu",lambda x: app.navigation_draw()]]
                right_action_items : [["bell",lambda x: app.navigation_draw()]]
                elevation : 10
            MDLabel:
                title : ''
    
"""