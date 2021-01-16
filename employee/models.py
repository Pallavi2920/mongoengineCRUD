from mongoengine import Document, fields, connect
connect('employee')

# Create your models here.
class Employee(Document):
    first_name = fields.StringField(max_length=50)
    last_name = fields.StringField(max_length=50)
    email = fields.EmailField(required=True,unique=True)
    dob = fields.StringField(max_length=150)
