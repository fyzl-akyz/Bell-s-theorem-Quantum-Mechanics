from random import randint, choice
import time
import colorama
from colorama import Fore, Back, Style
print("Detector 1 was selected as 0 degrees.")
detector2_degree = int(input("   1 - 0 degree \n   2 - 120 degree \n Choose for Detector 2 :   "))
test_count = int(input(" Count :   "))
for x in range(test_count):
    print("---------------- \n Count : ",x)
    time.sleep(3)
    print("\nSuccessfully sent to 2 particle detectors \n")
    if (((detector2_degree == 2))  ):
        spin = randint(0,1)
        if ( spin ==0):
            value = randint(1,100)
            if value <=75:
                print('Particles Spin ways : \n ')
                print(Fore.RED)
                print('    Detector 1 Result :   ↑    %50 ')
                print('    Detector 2 Result :   ↘    %75')
                print(Style.RESET_ALL)
            else:
                print('Particles Spin ways : \n ')
                print(Fore.RED)
                print('    Detector 1 Result :   ↑    %50\n')
                print(Fore.GREEN)
                print('    Detector 2 Result :   ↖    %25')
                print(Style.RESET_ALL)
        elif(spin == 1 ):
            value2 = randint(1, 100)
            if value2 <= 75:
                print('Particles Spin ways : \n ')
                print(Fore.RED)
                print('    Detector 1 Result :   ↓    %50\n    Detector 2 Result :   ↖    %75')
                print(Style.RESET_ALL)
            else:
                print('Particles Spin ways : \n ')
                print(Fore.RED)
                print('    Detector 1 Result :   ↑    %50\n    ')
                print(Fore.GREEN)
                print('Detector 2 Result :   ↘    %25')
                print(Style.RESET_ALL)
    elif (  (detector2_degree == 1)):
        spin = randint(0, 1)
        if (spin == 0):
            print('Particles Spin ways : \n ')
            print('    Detector 1 Result :   ↑    %50\n    Detector 2 Result :   ↓    %50')
        else:
            print('Particles Spin ways : \n ')
            print('    Detector 1 Result :   ↓    %50\n    Detector 2 Result :   ↑    %50')
