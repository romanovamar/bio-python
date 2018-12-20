import os
import sys
import argparse

sys.path.insert(1, '../task9.py')
from task9 import *


def main(args):
    print('\n\n\33[92m'
          '$$\       $$\                     $$\ \n'
          '$$ |      \__|                    $$ |       \n'
          '$$$$$$$\  $$\  $$$$$$\   $$$$$$$\ $$$$$$$\'  \n'
          '$$  __$$\ $$ |$$  __$$\ $$  _____|$$  __$$\ \n'
          '$$ |  $$ |$$ |$$ /  $$ |\$$$$$$\  $$ |  $$ | \n'
          '$$ |  $$ |$$ |$$ |  $$ | \____$$\ $$ |  $$ | \n'
          '$$$$$$$  |$$ |\$$$$$$  |$$$$$$$  |$$ |  $$ | \n'
          '\_______/ \__| \______/ \_______/ \__|  \__| \n'
          '\33[0m\n\n')
    cwd = Directory(os.getcwd())
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd.path)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        if cmd == 'ls':
            print()
            path = cwd.path if not cmdargs else cmdargs[0]
            directory = cwd.getsubdirectory(path)
            for item in directory.items():
                if item.isfile():
                    print('{name}\tFILE\t{size}'.format(name=item.getname(), size=len(item)))
                else:
                    print('{name}\tDIR'.format(name=item.getname()))
            print()

        elif cmd == 'cd':
            try:
                if cmdtokens[1] == '..':
                    main(os.chdir(os.path.split(os.getcwd())[0]))
                else:
                    main(os.chdir(cmdtokens[1]))
            except FileNotFoundError:
                print(f'Directory {cmdtokens[1]} not found')

        elif cmd == 'cat':
            file = File(cmdargs[0])
            try:
                for lines in file.getcontent():
                    print(lines)
            except FileNotFoundError:
                print(f'File not found')


        elif cmd == 'head':
            file = File(cmdargs[0])
            try:
                for lines in File.getcontent(file)[:10]:
                    print(lines)
            except FileNotFoundError:
                print(f'File not found')

        elif cmd == 'tail':
            try:
                file = File(cmdargs[0])
                for lines in File.getcontent(file)[-10:]:
                    print(lines)
            except FileNotFoundError:
                print(f'File not found')

        elif cmd == 'pwd':
            print(os.getcwd())

        elif cmd == 'touch':
            pass


        elif cmd == 'find':
            pass


        elif cmd == 'exit':
            print("Bye bye!")
            break

        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))



if __name__ == '__main__':
    main(sys.argv)


