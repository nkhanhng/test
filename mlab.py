
import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds147265.mlab.com:47265/projectphonemarker

host = "ds147265.mlab.com"
port = 47265
db_name = "projectphonemarker"
user_name = "bach"
password = "bach"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
