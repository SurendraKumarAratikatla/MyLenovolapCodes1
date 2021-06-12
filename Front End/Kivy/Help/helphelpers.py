
screen_help = """
<TooltipMDIconButton@MDIconButton+MDTooltip>
#:import MDChips kivymd.uix.chip.MDChip
#:import partial functools.partial

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
    AboutRationScreen:

    # about user
    UserLoginScreen:
    UserShopItemsScreen:
    #UserRationStoreScreen:
    UserNonVegScreen:
    
    
    # user individual items creation
    UserEggsScreen:
    
    
    
    
    
    

<MenuScreen>:
    name: 'menu'

    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color

    MDLabel:
        text: 'Help VZM'
        font_style: 'H6'
        pos_hint: {'center_x':0.86,'center_y':0.6}
        theme_text_color: "Custom"
        text_color: rgba('#0e1574ff')
        elevation_normal: 10

    MDFloatingActionButton:
        icon: "bike"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'allitems'
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



<UserLoginScreen>:
    name: 'userlogin'
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
        hint_text : "Enter your shop address"
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
        on_press: root.manager.current = 'usershopitems'
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




<UserShopItemsScreen>:
    name: 'usershopitems'
    
    MDLabel:
        text: 'Choose below your shop/store type'
        font_style: 'Subtitle1'
        pos_hint: {'center_x':0.6,'center_y':0.9}
    
    MDChip:
        label: 'Ration-Store'
        icon: 'basket-fill'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.8}
        check: True
        callback: app.ration_store_chip
    MDChip:
        label: 'Non-Veg'
        icon: 'egg'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.7}
        check: True
        callback: app.non_veg_chip
        
    MDChip:
        label: 'Vegetables'
        icon: 'leaf'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.6}
        check: True
        callback: app.vegetables_chip
    MDChip:
        label: 'Fruits'
        icon: 'fruit-grapes'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.5}
        check: True
        callback: app.fruits_chip
    MDChip:
        label: 'Sports-Kits'
        icon: 'cricket'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.4}
        check: True
        callback: app.sports_kits_chip
    MDChip:
        label: 'Street Food'
        icon: 'food-fork-drink'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.3}
        check: True
        callback: app.street_food_chip
    
    MDChip:
        label: 'Others'
        icon: 'warehouse'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.2}
        check: True
        callback: app.others_chip
        
    MDRoundFlatButton:
        text: "Next"
        text_color: 0, 1, 0, 1
        elevation_normal: 12
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: root.manager.current = 'usernonveg'
            
            

# UserRationStoreScreen:
#     name: 'userration'

<UserNonVegScreen>:
    name: 'usernonveg'
    MDLabel:
        text: 'Select available non-veg in your shop'
        font_style: 'Subtitle1'
        pos_hint: {'center_x':0.6,'center_y':0.9}
    
    MDChip:
        label: 'Eggs'
        icon: 'egg'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.7}
        check: True
        callback: app.ration_store_chip
    MDChip:
        label: 'Chicken'
        icon: 'egg-easter'
        elevation_normal: 10
        pos_hint: {'center_x':0.5,'center_y':0.5}
        check: True
        callback: app.non_veg_chip
        
    MDRoundFlatButton:
        text: "Back"
        text_color: 0, 1, 0, 1
        elevation_normal: 12
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: root.manager.current = 'usershopitems'
        
    MDRoundFlatButton:
        text: "Next"
        text_color: 0, 1, 0, 1
        elevation_normal: 12
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: root.manager.current = 'usereggs'



# user individual items creation


<UserEggsScreen>:
    name: 'usereggs'
    shopname: user_eggs_shopname_box
    eggrate: user_eggs_eggrate_box
    eggtrayrate: user_eggs_eggtray_box
    
    
    MDLabel:
        text: 'Prepare your shop by entering below details '
        font_style: 'Subtitle1'
        pos_hint: {'center_x':0.6,'center_y':0.8}
        
        
    # MDTextField:
    #     #hint_text: "Rectangle mode"
    #     mode: "rectangle"
    #     id : user_eggs_shopname_box
    #     icon_left: "home"
    #     size_hint: 1, None
    #     hint_text: "Enter your shop name"
    #     pos_hint : {'center_x':0.5, 'center_y': 0.65}
    #     text_color: (0,1,0)
    #     #width : 300
    #     height: "30dp"
    MDTextField:
        id : user_eggs_shopname_box
        write_tab: False
        mode: "rectangle"
        foreground_color : [0,0,1,1]
        hint_text : "Enter your shop name"
        #required: True
        #max_text_length : 30
        helper_text_mode : "on_focus"
        icon_right : "home"
        #icon_right_color: [0,1,0,1]
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y': 0.65}
        text_color: (0,1,0)
        size_hint_x : None
        width : 300
    MDTextField:
        id: user_eggs_eggrate_box
        mode: "rectangle"
        write_tab: False
        hint_text : "Enter single egg rate in Rs"
        #max_text_length : 10
        #required: True
        helper_text_mode: "on_error"
        helper_text_mode : "on_focus"
        icon_right : "egg"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y': 0.5}
        size_hint_x : None
        width : 300
    MDTextField:
        id: user_eggs_eggtray_box
        mode: "rectangle"
        write_tab: False
        #multiline: True
        hint_text : "Enter one tray rate in Rs"
        #required: True
        #max_text_length : 10
        helper_text_mode : "on_focus"
        icon_right : "egg"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x':0.5, 'center_y': 0.35}
        size_hint_x : None
        width : 300
        
    MDRectangleFlatButton:
        text : 'Submit'
        pos_hint : {'center_x':0.5,'center_y':0.15}
        elevation_normal: 9
        on_press: root.add_user()
        on_press: root.manager.current = 'eggs'
        #on_release: self.AllItemsScreen
        
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Eggs Store'
                left_action_items : [["clock",lambda x: app.navigation_draw()]]
                right_action_items : [["cart-plus",lambda x: app.navigation_draw()]]
                #left_action_items : [["egg",lambda x: app.navigation_draw()]]
                #pos_hint: {'center_x':0.1,'center_y':0.8}
                elevation : 10
            MDLabel:
                title : ''
                
    
                
        
    
    
    
    
    
    
    
    
    
    

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
                            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                            right_action_items: [["shopping-search", lambda x: app.navigation_draw_1()],["clock", lambda x: app.show_time_picker()]]
                            # MDTextField:
                            #     id: search_field
                            #     hint_text: 'Search Product'
                            #     #on_text: root.set_list_md_icons(self.text, True)
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
                        icon: 'plus'
                        callback: app.callback
                        opening_transition_button_rotation: 'out_cubic'
                        #callback: app.data
                        data: app.data
                        elevation_normal: 12
                        rotation_root_button: True
                        bg_hint_color: app.theme_cls.primary_light
                        #pos_hint: {'left':0.5,'right':0.5}
                        hint_animation : True
                        #bg_color_root_button: 0, 0, 1, 1
                        #right_pad: True
            MDNavigationDrawer:
                type: "standard"
                #anchor : "right"
                #close_on_click: False
                #state : "close"
                id: nav_drawer
                #closing_transition : "in_sine"
                closing_time : 0.1
                
                
                
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
                                    on_press: root.manager.current = 'userlogin'
                                    IconLeftWidget:
                                        icon: "account-multiple-check"

                                    FloatLayout:
                                        MDSwitch:
                                            pos_hint: {'center_x': 0.9, 'center_y': 0}
                                
                                OneLineIconListItem:
                                    text: "Change Theme"
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    on_release: app.show_theme_picker()
                                    IconLeftWidget:
                                        icon: "invert-colors"
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
                                icon: "bell"
                                #pos_hint: {'center_x':0.1,'center_y':0.1}
                                on_press: root.manager.current = 'allitems'

                        Widget:

                        MDBottomAppBar:
                            MDToolbar:
                                #title : 'Help'
                                icon :'reply'
                                elevation_normal: 12
                                #left_action_items: [['menu', lambda x: lambda x: app.navigation_draw()]]
                                #on_action_button: app.about_draw()
                                on_action_button: root.manager.current = 'allitems'
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
                
#:import Label kivy.uix.label.Label
<FreshEggsScrren>:
    name: 'eggs'
    # MDScreen:
    #     radius: [25, 0, 0, 0]
    #     md_bg_color: app.theme_cls.primary_color

    # GridLayout:
    #     cols: 1
    #     on_parent:
    #         for item in range(3): text= "{0}".format(item);
    #         icon: "egg-easter"
    #         pos_hint: {'center_x':0.5,'center_y':0.7}
    #         #on_press: root.manager.current = 'profile'
    #         elevation_normal: 12
    
    GridLayout:
        cols: 3
        on_parent:
            for i in range(10): txt = "Label {0}".format(i); self.add_widget(Label(text = txt, text_size=(cm(2), cm(2)), pos=self.pos,
            id=txt, color=(1,1,1,1)))
            
            
            
        MDFillRoundFlatIconButton:
            text: root.data_items1[3]
            icon: "egg"
            pos_hint: {'center_x':0.5,'center_y':0.5}
            #on_press: root.manager.current = 'profile'
            elevation_normal: 12
            
    
    
    # MDFillRoundFlatIconButton:
    #     text: root.data_items1[3]
    #     icon: "egg"
    #     pos_hint: {'center_x':0.5,'center_y':0.5}
    #     #on_press: root.manager.current = 'profile'
    #     elevation_normal: 12
    
    
    # BoxLayout:
    #     orientation: "vertical"
    # 
    #     GridLayout:
    #         size_hint: 1, None
    #         size_hint_y: None
    #         height: 25
    #         cols: 2
    # 
    #         Label:
    #             text: "User ID"
    #         Label:
    #             text: "User Name"
    # 
    #     BoxLayout:
    #         RecycleView:
    #             viewclass: 'FreshEggsScrren'
    #             data: [{'text': str(x)} for x in root.data_items1]
    #             cols: 2
    #             default_size: None, dp(26)
    #             default_size_hint: 1, None
    #             size_hint_y: None
    #             #height: self.minimum_height
    #             orientation: 'vertical'
    #             multiselect: True
    #             touch_multiselect: True
    #             
    #             
    #             MDFillRoundFlatIconButton:
    #                 text: root.data_items1[0]
    #                 icon: "egg-easter"
    #                 pos_hint: {'center_x':0.5,'center_y':0.7}
    #                 #on_press: root.manager.current = 'profile'
    #                 elevation_normal: 12
    
    
    
    
    
    
    
    
    
    

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