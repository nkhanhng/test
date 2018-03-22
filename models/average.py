from mongoengine import *
from models.phone import Phone

class Average(Document):
    phone = ReferenceField(Phone)
    averagePoint = FloatField()
