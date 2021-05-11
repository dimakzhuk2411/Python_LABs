import os
import re
import hashlib
import subprocess

input_text = input('Введите текст: ') #text = 'Petr93 Johnny70 Service2002 5P1234'

def check_input(text, reg):
    for i in range(len(text)):
        parser = re.search(reg,text[i])
        count = 0
        while parser!=None:
            yield i+1,parser.regs[0][0] + count + 1, parser.group()
            count += parser.regs[0][1]
            text[i] = text[i][parser.regs[0][1]:]
            parser = re.search(reg,text[i])

reg = "[A-ZА-ЯЁ][A-ZА-ЯЁa-zа-яё]+([0-9]{4}$|[0-9]{2}$)"
[print(output_text) for i, j, output_text in check_input(input_text.split(),reg)]
