import mlab
from models.phone import Phone

mlab.connect()

phone_list = Phone.objects() #product_name="samsung"
first_phone = phone_list[0]

print(first_phone.to_mongo())
