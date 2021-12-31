import os

def create_directory_low():
    for x in range(1, 10):
        path = f'/home/jared/github/100daysofpython/day-00{x}'
        pathExists = os.path.exists(path)
        if not pathExists:
            os.makedirs(path)
            print(f'{path} is created')
        else:
            print(f'{path} already exists')

def create_directory_mid():
    for x in range(10, 100):
        path = f'/home/jared/github/100daysofpython/day-0{x}'
        pathExists = os.path.exists(path)
        if not pathExists:
            os.makedirs(path)
            print(f'{path} is created')
        else:
            print(f'{path} already exists')

def create_directory_high():
    for x in range(100, 101):
        path = f'/home/jared/github/100daysofpython/day-{x}'
        pathExists = os.path.exists(path)
        if not pathExists:
            os.makedirs(path)
            print(f'{path} is created')
        else:
            print(f'{path} already exists')

create_directory_low()
create_directory_mid()
create_directory_high()