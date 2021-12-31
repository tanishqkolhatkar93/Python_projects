import data
from data import balance, pin

while True:
    print("Welcome to SBI Bank")
    print("CARD INSERTED Y/N")
    chances = 3
    t = 0
    check_card = input("Y/N: ").upper()
    if(check_card == 'Y'):
        while(t<chances):
            if(t!=chances):
                x = int(input("Enter thr 4 digit pin: "))
                if(pin == x):
                    while True:
                        print("Enter 1 to Withdraw")
                        print("Enter 2 for Balance Inquiry")
                        print("Enter 3 to change pin")
                        print("Enter 4 to  transfer money to another SBI account")
                        print("Enter 5 to Remove ATM Card")
                        print()
                        enter = int(input(""))
                        if(enter == 2):
                            print(f"Balance is {balance}")
                            print()
                            
                        elif(enter == 5):
                            t = chances
                            break
                        elif(enter == 3):
                            pin = int(input("Enter the new pin: "))
                            
                        elif(enter == 1):
                            withdraw = int(input("Enter the amout you want to withdraw: "))
                            if(withdraw<=balance - 5000):
                                print(f"Your balance is {balance}, you cannot withdraw more than {balance - 5000}")
                                print()
                            else:
                                balance = balance - withdraw
                                print(f"Balance left is {balance}")
                                print()
                        else:
                            print("Retry")
                else:
                    t = t + 1
                    if(t  ==  chances):
                        print('Card Blocked')
                        print()
                        print()
                        break
                    else:
                         print(f'{chances-t} attempts left')
                         print()
                         print()
                    
            
            
                    
            
    
    
    
    
    
