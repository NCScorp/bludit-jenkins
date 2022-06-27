from datetime import datetime
import json
# args = 'j i v1 jenkinsv2 b f p'.split()

# argv = sys.argv[1:]

# try:
#     opts, args = getopt.getopt(argv, "j:i:v1:jenkinsv2:b:f:p:")
# except:
#     print("Erro nos opts e args")

# for opt, arg in opts:
#     if opt in ['-t']:
#         t = arg
#     elif opt in ['-v']:
#         v = arg

# print(v + ' ' + t)


# def fodase(foda):
#     return json

# x = """{
#     "Name": "Jennifer Smith",
#     "Contact Number": 7867567898,
#     "Email": "jen123@gmail.com",
#     "Hobbies":["Reading", "Sketching", "Horse Riding"]
# }"""

# print(fodase(x))

# pay = {'changeSet':{'items':[{ "0":"teste", "1": "tes1" }]}}

# print(pay['changeSet']['items'])

class Teste:
    def __init__(self, json):
        self._json = json

    @property
    def jsonObj(self):
        return str(self._json)

    @jsonObj.setter
    def jsonObj(self, json):
        self._json = str(json)
    
    def zica(self, zz):
        return f"zz {zz}"
    
    def ray(self):
        return []

    
x = Teste({"key": "value"})
print(x.jsonObj)

x.jsonObj = {"opa": "bão"}
print(x.jsonObj)

print(x.zica("itaa"))

x.ray = ["teste", "sasa", 2, "zae"]

print(x.ray)
print(type(x.ray))
