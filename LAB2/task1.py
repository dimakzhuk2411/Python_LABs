import os
import re
import hashlib
import subprocess

def count_letters():
    file = open('task1.txt')
    input_text = file.read()
    file.close()
    dictionary = {i.upper(): input_text.count(i) for i in input_text if i.isalpha()}
    for value in sorted(dictionary.keys(), key=dictionary.get, reverse=True):
        print(value, " --- ", dictionary[value])

count_letters()
