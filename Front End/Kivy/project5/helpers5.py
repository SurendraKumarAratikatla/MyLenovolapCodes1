screen_help = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    AllItemsScreen:
    RationScreen:
    BellScreen:
    NotificationScreen:
    #PropertyScreen:
    #DailyLaborScreen:
   #LocalJobs:
    FreshEggsScrren:
    # ItemDrawer:
    AboutScreen:
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
        id : mobile_number
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
                left_action_items : [["clock",lambda x: app.navigation_draw()]]
                right_action_items : [["shopping-search",lambda x: app.navigation_draw()]]
                #left_action_items : [["egg",lambda x: app.navigation_draw()]]
                #pos_hint: {'center_x':0.1,'center_y':0.8}
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

        NavigationLayout:
    
            ScreenManager:
    
                Screen:
    
                    BoxLayout:
                        orientation: 'vertical'
    
                        MDToolbar:
                            title: "VZM Store"
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                            right_action_items: [['shopping-music', lambda x: app.navigation_draw()]]
                        Widget:
                        
                        MDBottomAppBar:
                            MDToolbar:
                                #title : 'Help'
                                icon :'plus'
                                elevation: 10
                                #left_items: 'egg'
                                right_action_items: [['history', lambda x: lambda x: app.navigation_draw()]]
                                left_action_items: [['home', lambda x: lambda x: app.navigation_draw()]]
                                on_action_button: app.about_draw()
                                #on_press: root.manager.current = 'about'
                                mode: 'center'
                                type: 'bottom'
                                # MDIconButton:
                                #     icon: "home"
                                #     #pos_hint: {'left':3,'right':0.2}
                                #     on_press: root.manager.current = 'allitems'
                            
            MDNavigationDrawer:
                id: nav_drawer
    
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    padding: "8dp"
                    spacing: "8dp"
                    AnchorLayout:
                        anchor_x: "left"
                        size_hint_y: None
                        height: avatar.height
                        Image:
                            id: avatar
                            size: "56dp", "56dp"
                            size_hint: None, None
                            #size_hint: (1,1)
                            source: "mine.jpg"
                    MDLabel:
                        text: "Surendra"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "surendrachinna1341@gmail.com"
                        size_hint_y: None
                        font_style: "Caption"
                        height: self.texture_size[1]
                    ScrollView:
                        DrawerList:
                            id: md_list
                            
                            MDList:
                                OneLineIconListItem:
                                    text: "Profile"
                                
                                    IconLeftWidget:
                                        icon: "account"
                                        
                               
                                        
                                OneLineIconListItem:
                                    text: "Upload"
                                
                                    IconLeftWidget:
                                        icon: "upload"
                                        
                               
                                OneLineIconListItem:
                                    text: "Logout"
                                
                                    IconLeftWidget:
                                        icon: "logout"
                                        
                                OneLineIconListItem:
                                    text: "Starred"
                                
                                    IconLeftWidget:
                                        icon: "star"
                                        
                                OneLineIconListItem:
                                    text: "Recent"
                                
                                    IconLeftWidget:
                                        icon: "history"

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

        NavigationLayout:
    
            ScreenManager:
    
                Screen:
    
                    BoxLayout:
                        orientation: 'vertical'
    
                        MDToolbar:
                            title: "Ration Store"
                            elevation: 10
                            #left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                            MDIconButton:
                                icon: "arrow-left"
                                #pos_hint: {'center_x':0.1,'center_y':0.1}
                                on_press: root.manager.current = 'allitems'
    
                        Widget:
                        
                        MDBottomAppBar:
                            MDToolbar:
                                #title : 'Help'
                                icon :'head-question'
                                elevation: 10
                                #left_action_items: [['menu', lambda x: lambda x: app.navigation_draw()]]
                                on_action_button: app.about_draw()
                                #on_press: root.manager.current = 'about'
                                mode: 'end'
                                type: 'bottom'
                                MDIconButton:
                                    icon: "home"
                                    pos_hint: {'right':4,'y':0}
                                    on_press: root.manager.current = 'allitems'
                                    
<NotificationScreen>:
    name: 'notification'
    MDLabel:
        text: 'No Notifications Found'
        font_style: 'H6'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDFloatingActionButton:
        icon: "bell"
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
        elevation_normal: 10
        #on_release: self.ProfileScreen
                                
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
        #on_release: self.ProfileScreen
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
    MDFillRoundFlatIconButton:
        text: "Individual"
        icon: "egg"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        #on_press: root.manager.current = 'profile'
        elevation_normal: 12

    Screen:

        NavigationLayout:
    
            ScreenManager:
    
                Screen:
    
                    BoxLayout:
                        orientation: 'vertical'
    
                        MDToolbar:
                            title: "Fresh Eggs Store"
                            elevation: 10
                            #left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                            MDIconButton:
                                icon: "arrow-left"
                                #pos_hint: {'center_x':0.1,'center_y':0.1}
                                on_press: root.manager.current = 'ration'
    
                        Widget:
                        
                        MDBottomAppBar:
                            MDToolbar:
                                #title : 'Help'
                                icon :'head-question'
                                elevation: 10
                                on_action_button: app.about_draw()
                                #on_press: root.manager.current = 'about'
                                mode: 'end'
                                type: 'bottom'
                                MDIconButton:
                                    icon: "home"
                                    #pos_hint: {'center_x':0.1,'center_y':0.1}
                                    on_press: root.manager.current = 'allitems'
           
# <ItemDrawer>:
#     theme_text_color: "Custom"
#     on_release: self.parent.set_color_item(self)
# 
#     IconLeftWidget:
#         id: icon
#         icon: root.icon
#         theme_text_color: "Custom"
#         text_color: root.text_color

<AboutScreen>:
    name: 'about'
    Screen:
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "280dp", "180dp"
            pos_hint: {"center_x": .5, "center_y": .5}

            MDLabel:
                text: "Help"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]
    
            MDSeparator:
                height: "1dp"
    
            MDLabel:
                text: "Gathering here all store items in VZM "



"""