# import argparse

# parse = argparse.ArgumentParser(description="Flags do programa")
# parse.add_argument('-v', nargs='*', help="teste with v")
# parse.add_argument('-l', help="teste with l")

# args = parse.parse_args()


# if args.v:
#     if "zeca" in args.v:
#         print("opa, esse não!")
#     else:
#         print("este é com v: ",args.v)
#         argu = args.v
#         print(argu[0], argu[1])
# if args.l:
#     print("Este é com L:",args.l)
# from datetime import datetime
# import json
# import getopt
# import re
# import sys

# argv = sys.argv[1:]
# tuples = []
# v,l='',''
# try:
#     opts, args = getopt.getopt(argv, "v:l:")
# except:
#     print("deu ruim")

# print(opts)

# for opt, arg in opts:
#     if opt in ['-v']:
#         v = tuples.append(tuple(re.split(r' ', arg)))
#     elif opt in ['-l']:
#         l = arg

# print(v, l)
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
    
    def lebo(self):
        return "opa vle"

    
x = Teste({"key": "value"})
print(x.jsonObj)

x.jsonObj = {"opa": "bão"}
print(x.jsonObj)

print(x.zica("itaa"))

print(x.lebo())