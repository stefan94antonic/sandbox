#!/usr/bin/python3
import os
import time

# key = open('/media/tony/Key/key', 'r')
# print(key.read())
#


while True:
    try:
        key = open('/media/tony/Key/.key', 'r')
        shape = key.read()
        shape = shape.replace('\n', '')

        lock = open("/home/tony/skripte/.brava", 'r')
        brava = lock.read()
        brava = brava.replace("\n", 'r')

        if shape == brava:
            print('kljuc je u bravi')
            os.system("loginctl unlock-session")

        else:
            os.system("loginctl lock-session")
            pass
        key.close()
        lock.close()
    except:
        print('brava je prazna')
        os.system("loginctl lock-session")

    finally:
        time.sleep(1)

