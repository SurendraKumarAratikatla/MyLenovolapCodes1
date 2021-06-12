
screen_help = """
<TooltipMDIconButton@MDIconButton+MDTooltip>


ScreenManager:
    MenuScreen:
    UserCustomerScreen:
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
    AboutRationScreen:
<MenuScreen>:
    name: 'menu'

    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color

    MDLabel:
        text: 'VZM Store'
        font_style: 'H6'
        pos_hint: {'center_x':0.86,'center_y':0.6}
        theme_text_color: "Custom"
        text_color: rgba('#0e1574ff')
        elevation_normal: 10

    MDFloatingActionButton:
        icon: "shopping"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile'
        elevation_normal: 10
        #on_release: self.ProfileScreen

    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: rgba('#0e1574ff')
            Triangle:
                points: [0, self.size[1], self.size[0],self.size[1],0, self.size[1]-(.4*self.size[1])]

            Color:
                rgba: rgba('#0e1574c8')
            Triangle:
                points: [0, self.size[1], self.size[0],self.size[1],self.size[0], self.size[1]-(.4*self.size[1])]



<UserCustomerScreen>:
    name: 'usercustomer'
    # Screen:
    #     TooltipMDIconButton:
    #         icon: "face"
    #         tooltip_text: 'showcase your products to customers'
    #         pos_hint: {"center_x": 0.5, "center_y": 0.7}
    #         tooltip_text_color: 0, 0, 1, 1
    #         tooltip_bg_color: 0, 1, 0, 1
    #     TooltipMDIconButton:
    #         icon: "language-python"
    #         tooltip_text: self.icon
    #         pos_hint: {"center_x": 0.5, "center_y": 0.5}
    Screen:
        MDFloatingActionButtonSpeedDial:
            data: app.data
            elevation: 10
            rotation_root_button: True
            pos_hint: {'left':0.8,'right':0.6}


<ProfileScreen>:
    name: 'profile'
    mobile: mobile_box
    user: user_box
    address: address_box

    MDTextField:
        id : mobile_box
        write_tab: False
        foreground_color : [0,0,1,1]
        hint_text : "Enter mobile number"
        #required: True
        max_text_length : 10
        helper_text_mode : "on_focus"
        icon_right : "cellphone-android"
        #icon_right_color: [0,1,0,1]
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y': 0.6}
        text_color: (0,1,0)
        size_hint_x : None
        width : 300
    MDTextField:
        id: user_box
        write_tab: False
        hint_text : "Enter your name"
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
        id: address_box
        write_tab: False
        #multiline: True
        hint_text : "Enter address"
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
        on_press: root.add_user()
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
                right_action_items : [["cart-plus",lambda x: app.navigation_draw()]]
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
                    MDFloatingActionButton:
                        icon: "basket-fill"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
                        on_press: root.manager.current = 'aboutration'

            OneLineAvatarIconListItem:
                text : 'Property'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "home-city"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Daily Labor Workers'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "nature-people"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10

            OneLineAvatarIconListItem:
                text : 'Hospitals'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "hospital"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'House for sale'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "home"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10

            OneLineAvatarIconListItem:
                text : 'House for rent'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "home-city"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Sarees'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "face-profile-woman"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Cloths for men'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "tshirt-crew"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Cloths for women'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "face-profile-woman"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Dry Fruits'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "fruit-cherries"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Fruits'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "fruit-grapes"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Study Rooms'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "pen"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Sports'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "cricket"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Wholesale Shopes'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "bag-carry-on"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10
            OneLineAvatarIconListItem:
                text : 'Local Jobs'
                IconLeftWidget:
                    MDFloatingActionButton:
                        icon: "email-search"
                        md_bg_color: 180/255.0,120/255.0,219/255.0,1
                        #size: [6]
                        btn_size: (40,40)
                        size: (45,45)
                        elevation_normal: 10

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
                            right_action_items: [['bell', lambda x: app.navigation_draw()]]
                        Widget:

                        # MDBottomAppBar:
                        #     MDToolbar:
                        #         #title : 'Help'
                        #         icon :'plus'
                        #         elevation_normal: 10
                        #         #left_items: 'egg'
                        #         right_action_items: [['history', lambda x: lambda x: app.navigation_draw()]]
                        #         left_action_items: [['home', lambda x: lambda x: app.navigation_draw()]]
                        #         on_action_button: app.plus_action()
                        #         #on_press: root.manager.current = 'about'
                        #         mode: 'center'
                        #         type: 'bottom'
                        #         # MDIconButton:
                        #         #     icon: "home"
                        #         #     #pos_hint: {'left':3,'right':0.2}
                                #     on_press: root.manager.current = 'allitems'

                    MDFloatingActionButtonSpeedDial:
                        data: app.data
                        elevation_normal: 12
                        rotation_root_button: True
                        #pos_hint: {'left':0.5,'right':0.5}
                        #hint_animation : True
                        bg_color_root_button: 0, 0, 1, 1
                        #right_pad: True
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
                        #on_press: root.manager.current = 'profile'
                        text: 'Surendra'
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
                                    text: "Starred"

                                    IconLeftWidget:
                                        icon: "star"

                                OneLineIconListItem:
                                    text: "Recent"

                                    IconLeftWidget:
                                        icon: "history"

                                OneLineIconListItem:
                                    text: "Login as a user"
                                    on_press: root.manager.current = 'profile'
                                    IconLeftWidget:
                                        icon: "account-multiple-check"

                                    FloatLayout:
                                        MDSwitch:
                                            pos_hint: {'center_x': 0.9, 'center_y': 0}
                                OneLineIconListItem:
                                    text: "Logout"
                                    on_press: root.manager.current = 'profile'
                                    IconLeftWidget:
                                        icon: "logout"


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


<AboutRationScreen>:
    name: 'aboutration'
    Screen:
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "280dp", "180dp"
            pos_hint: {"center_x": .5, "center_y": .5}

            MDLabel:
                text: "About Ration Store"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]

            MDSeparator:
                height: "1dp"

            MDLabel:
                text: "Here you can find daily ration things as you needed in your home, please step in and order at your door step.."
    MDFloatingActionButton:
        icon: "thumb-up"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'allitems'
        elevation_normal: 10
        #on_release: self.ProfileScreen
        #md_bg_color: 180/255.0,120/255.0,219/255.0,1
        #size: [6]
        btn_size: (40,40)
        size: (45,45)



"""