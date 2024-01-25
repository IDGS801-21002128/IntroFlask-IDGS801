from wtForms import *
class UserForm(Form):
    nombre = StringField('nombre')
    email = StringField('email')
    apaterno=TelField('apaterno')