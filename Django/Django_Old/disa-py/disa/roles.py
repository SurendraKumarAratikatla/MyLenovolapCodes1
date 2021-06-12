from rolepermissions.roles import AbstractUserRole

class Member(AbstractUserRole):
    available_permissions = {
        'VIEW_SELF_DETAILS' : True,
        'EDIT_MEMBER_DETAILS' : True,
        'EDIT_MEMBER_SEVAS'   : True,       
        'EDIT_MEMBER_ADDRESS' : True,
        'ADD_MEMBER_ADDRESS'  : True,
       }

class Staff(AbstractUserRole):
    available_permissions = {
        'VIEW_MEMBER_DETAILS' : True,
        'ADD_MEMBER_DETAILS'  : True,
        'EDIT_MEMBER_DETAILS' : True,
        'EDIT_MEMBER_SEVAS'   : True,
        'ADD_MEMBER_SEVAS'    : True,
        'EDIT_MEMBER_ADDRESS' : True,
        'ADD_MEMBER_ADDRESS'  : True,
        'EXPORT_REPORTS'      : True,
        'VIEW_ORGANISATION'   : True,
        'VIEW_SEVA_CATEGORY'  : True,
      }

class Admin(AbstractUserRole):
    available_permissions = {
        'VIEW_SELF_DETAILS'   : False,
        'VIEW_MEMBER_DETAILS' : True,
        'EDIT_MEMBER_DETAILS' : True,
        'ADD_MEMBER_DETAILS'  : True,
        'VIEW_MEMBER_SEVAS'   : True,
        'EDIT_MEMBER_SEVAS'   : True,
        'ADD_MEMBER_SEVAS'    : True,
        'EDIT_MEMBER_ADDRESS' : True,
        'ADD_MEMBER_ADDRESS'  : True,
        'EXPORT_REPORTS'      : True,
        'ASSIGN_OPERATOR'     : True,
        'ADD_ORGANISATION'    : True,
        'EDIT_ORGANISATION'   : True,
        'VIEW_ORGANISATION'   : True,
        'ADD_SEVA_CATEGORY'   : True,
        'EDIT_SEVA_CATEGORY'  : True,
        'VIEW_SEVA_CATEGORY'  : True,
        'EXPORT_DB'           : True,
        'SEND_CUSTOM_MESSAGE' : True,
        'ACCESS_CONTROL'      : True,
        'ASSIGN_OPERATOR'     : True,
        'ADD_MEMBERSHIP'      : True,
        'VIEW_MEMBERSHIP'     : True,
        'EDIT_MEMBERSHIP'     : True,
        'ADD_MEDICALPROFILE'  : True,
        'EDIT_MEDICALPROFILE' : True,
     }

class SuperAdmin(AbstractUserRole):
     available_permissions = {
        'ACCESS_CONTROL'      : True,
        'ASSIGN_ADMIN'   : True,
     }
