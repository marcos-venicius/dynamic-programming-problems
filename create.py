#!/usr/env/bin python3

import os
import sys

def read_name():
    if len(sys.argv) >= 2:
        return sys.argv[1]

    name = input('challenge name: ')

    if len(name.strip()) == 0:
        return read_name()

    return name;

class CreateNewWorkDir(object):
    def __init__(self):
        self.name = None
        self.last_dir_number = None
        self.files = {}
        self.improved_version = self.check_is_improved_version()
        self.code_file_name = "code.py"
        self.desc_file_name = "description.txt"

        self.load_files()

    def check_is_improved_version(self):
        for arg in sys.argv:
            if arg == 'improve':
                return True
        
        return False

    def load_files(self):
        for d in os.listdir('.'):
            self.files[d] = 1

    def copy_file_content(self, file):
        lines = []

        with open(file, 'rb') as f:
            lines = f.readlines()

        text = ""

        for line in lines:
            text += line.decode("utf-8")

        return bytes(text, 'utf-8')
    
    def get_last_dir_number(self, pad=2):
        m = 0

        for d in self.files:
            s = d.split('-')

            if s[0].isnumeric():
                n = int(s[0])
                m = max(n, m)

        if not self.improved_version:
            m += 1

        return str(m).rjust(pad, '0')

    def get_workdir_name_imp(self):
        m = 0
        dir_name = ""

        for d in self.files:
            s = d.split('-')

            if s[0].isnumeric():
                n = int(s[0])
                if n >= m:
                    m = n
                    dir_name = d

        if dir_name.endswith("-improve"):
            raise "a normal version not exists"

        self.name = f'{dir_name}-improve'
        self.get_last_dir_number()

    def get_workdir_name(self):
        if self.improved_version:
            self.get_workdir_name_imp()
        else:
            last_dir_number = self.last_dir_number if self.last_dir_number is not None else self.get_last_dir_number()

            name = self.name if self.name is not None else read_name()
            name = name.strip()
            name = f'{last_dir_number}-{name}'
            self.name = name
            self.last_dir_number = last_dir_number

    def create_workdir(self):
        self.get_workdir_name()

        os.mkdir(self.name)

        code_file = f'{self.name}/{self.code_file_name}'
        desc_file = f'{self.name}/{self.desc_file_name}'

        if self.improved_version:
            cname = self.name.replace("-improve", "")

            code_file = f'{self.name}/{self.code_file_name}'
            desc_file = f'{self.name}/{self.desc_file_name}'

            prev_code_file = f'{cname}/{self.code_file_name}'
            prev_desc_file = f'{cname}/{self.desc_file_name}'

            code_content = self.copy_file_content(prev_code_file)
            desc_content = self.copy_file_content(prev_desc_file)

            with open(code_file, 'wb') as f:
                f.write(code_content)
                f.close()

            with open(desc_file, 'wb') as f:
                f.write(desc_content)
                f.close()
        else:
            with open(code_file, 'wb') as f:
                f.write(b'#!/usr/bin/env python3')
                f.write(b'\n')
                f.close()

            with open(desc_file, 'wb') as f:
                f.write(b'Your challenge description')
                f.write(b'\n')
                f.close()

        if self.improved_version:
            print(f"created an improvement version of \"{cname}\" challenge")
        else:
            print(f"challenge \"{self.name}\" created successfully")


createNewWorkDir = CreateNewWorkDir()

createNewWorkDir.create_workdir()
