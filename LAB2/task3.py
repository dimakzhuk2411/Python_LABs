import os
import re
import hashlib
import subprocess

def replace_name_track():
    file_name = 'task3'
    with open('task3_track.txt') as f:
        for file in os.listdir(file_name):
            os.replace(file_name + '/' + file, file_name + '/' + f.readline().rstrip() + '.mp3')

replace_name_track()
