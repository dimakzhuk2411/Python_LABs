import os
import re
import hashlib
import subprocess

def search_duplicate_files():
    file_name = 'task2'
    files = os.listdir(file_name)
    nums = []
    for file in files:
        with open(file_name + '\\' + file) as file:
            nums.append(hashlib.md5(file.read().encode('utf-8')).hexdigest())

    for i in range(len(files) - 1):
        for j in range(i + 1, len(files)):
            if nums[i] == nums[j]:
                print('Группа дубликатов:', files[i], files[j])

search_duplicate_files()
