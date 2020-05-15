 from .decoder import JSONDecoder
from simplejson import JSONDecodeError
data='''
{
"name":"chuck"
"phone":{
"type":"intl",
"number":"+1 734 303 4456"
},
"email":{
"hide":"yes"
}
}'''
info=json.loads(data)
print('name;',info["name"])
print('Hide;',info["email"]["hide"])
