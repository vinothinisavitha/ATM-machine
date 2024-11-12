import time

print("Please insert your CARD")

time.sleep(5)

password=1234

pin=int(input("enter your atm pin"))

balance = 5000

if pin==password:
    while True:

        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """ 
            )

        try:
            option=int(input("Please enter your choice "))
        except:
            print("Please enter valid option")


        if option==1:
            print(f"your current balance is {balance}")
            print("=======================================")
            print("=======================================")
            print("=======================================")

        if option==2:

            withdraw_amount=int(input("Please enter withdraw_amount"))
            print("=======================================")
            print("=======================================")
            print("=======================================")

            balance=balance-withdraw_amount
            
            print("=======================================")
            print("=======================================")

            print(f"{withdraw_amount} is debited from your account")

            print("=======================================")
            print("=======================================")

            print(f"your updated balance is {balance}")

            print("=======================================")
            print("=======================================")

        if option==3:

            deposit_amount=int(input("please nter deposit_amount"))

            balance=balance+deposit_amount

            print("=======================================")
            print("=======================================")

            print(f"{deposit_amount} is creddited to your account")

            print("=======================================")
            print("=======================================")

            print(f"your updated balance is {balance}")

            print("=======================================")
            print("=======================================")

        if option==4:
        
            Break


    else:
        print("wrong pin Please try again")
