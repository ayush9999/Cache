import json
from collections import OrderedDict
import time
import os
 
if os.path.exists("qwerty.json"):
    record = json.load(open("qwerty.json", "r"), object_pairs_hook=OrderedDict)
else:
    record = OrderedDict({})

fo = open("foo.txt", "wb")

x = list(record.items())[-20:];
#x = list(record.items())[:20];
x2 = sorted(x, key=lambda k: k[1]['time'], reverse=True)
print(x2)
print (len(record))
print (len(x2))

command = ""
while command != 'exit':
    command = input('Enter a command(options: create,read,save): ')
    if command == "create":
        name = input('Enter name of the Student:')
        p = input('Student ID: ')
        a = input('Class: ')
        n = input('Marks: ')
        time = time.time()
 
        record[name] = {'Student ID:': p, 'Class:': a, 'Marks': n, 'time': time }
        json.dump(record, open('qwerty.json', "w"))
 
    elif command == 'read':
        z = json.load(open("qwerty.json", "r"), object_pairs_hook=OrderedDict)
        print(z)
 
    elif command == 'save':
        json.dump(record, open('qwerty.json', "w"))
        command = 'exit'

fo.close()