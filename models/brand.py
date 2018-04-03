from mongoengine import*

class Brand(Document):
    brand_name = StringField()
    logo = StringField()
    description = StringField()
