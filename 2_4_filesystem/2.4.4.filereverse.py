#!/usr/bin/python3

def filereverse(path):
    ''' function get file and save file with lines in reverse manner '''
    with open(path) as fi:
        lines = fi.read().split('\n')
        reversefilename = '{}_reverse'.format(path)
        with open(reversefilename, 'w') as reverse:
            for line in lines[-1::-1]:
                reverse.write(f'{line}\n')
        print(f'use cat {reversefilename} to check result')


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        script, path = argv
        filereverse(path)
    else:
        print("you need to run this script with 1 argument")
