
import time

def countdown(num):
    while num > 0:
        print(f'{num} SECOND(S)!')
        num -= 1
    print("HAPPY NEW YEAR!")

countdown(9)

def countdown_with_sleep(num):
    while num > 0:
        print(f'{num} SECOND(S)!')
        time.sleep(1)
        num -= 1
    print("HAPPY NEW YEAR!")
   

countdown_with_sleep(9)