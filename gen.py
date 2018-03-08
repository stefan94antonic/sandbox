#!/usr/bin/python3

import random

ran = ''.join([random.choice('0123456789abcdef') for x in range(32)])
print(ran)
try:
    brava = open("/home/tony/skripte/.brava",'w')
    brava.write(ran)
    brava.close()
except:
    pass
