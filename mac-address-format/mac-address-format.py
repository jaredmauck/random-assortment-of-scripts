import re
from rich import print

def mac_address_input():
    with open('macadd.txt', 'r') as macaddress:
        macaddresses = macaddress.read().splitlines()
        return macaddresses
#define function as variable
lines = mac_address_input()
#set choice to arbitrary number
choice = 100


while choice != 0:
    try:
        choice = int(input('Choose your format: 1 = xx:xx:xx:xx:xx:xx, 2 = xxxx.xxxx.xxxx, 3 = xxxxxx-xxxxxx, 4 = xxxxxxxxxxxx, or 0 if finished: '))
        for line in lines:
            nodelim = re.sub(r'[^a-fA-F0-9]', '', line).lower()
            if choice == 1:
                colon = ':'.join(nodelim[i:i + 2] for i in range(0, len(nodelim), 2))
                print(colon)
            elif choice == 2:
                period = '.'.join(nodelim[i:i + 4] for i in range(0, len(nodelim), 4))
                print(period)
            elif choice == 3:
                dash = '-'.join(nodelim[i:i + 6] for i in range(0, len(nodelim), 6))
                print(dash)
            elif choice == 4:
                print(nodelim)
        if choice == 0:
            print('Script Complete.')
        elif choice <= 4:
            choice = choice
        else:
            print('use an integer between 1-4 or 0 if finished')
    except ValueError:
        print('use an integer between 1-4 or 0 if finished')