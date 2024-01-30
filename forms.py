from wtforms import Form,StringField,EmailField,IntegerField,TelField

class UserForm(Form):
    nombre = StringField('nombre')
    email = EmailField('email')
    apaterno=TelField('apaterno')
    amaterno=TelField('amaterno ')
    numeroCelular=IntegerField('nCelular')