from mongoengine import *


class Evaluate(Document):
    phone = ReferenceField('Phone')
    design = IntField()
    screen = IntField()
    func = IntField()
    exp = IntField()
    cam = IntField()
    pin = IntField()
    comment = StringField()
