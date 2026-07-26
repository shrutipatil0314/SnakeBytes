balance = 0.0
kyc_documents={}

def check_balance():
    print()
    print("=========================================")  
    print(f"Your current balance is: ${balance}")
    print("=========================================")           
    print()
def deposit(amount):
    global balance
    if amount >= 0: 
     balance += amount
    else:
        print()
        print("=========================================")
        print("Invalid deposit amount.")
        print("=========================================")
        print()

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print()
        print("=========================================")
        print(f"Withdrew ${amount}. Your balance is: ${balance}")
        print("=========================================")
        print()
    else:
        print()
        print("=========================================")
        print("Invalid withdrawal amount or insufficient funds.")
        print("=========================================")
        print()

def kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents)==0:
        print()
        print("=========================================")
        print("kyc not done")
        print("=========================================")
        print()
    else:
        for doc in kyc_documents:
            
            print("=========================================")
            print(f"{doc}: {kyc_documents[doc]}")
            print("=========================================")
            


if __name__ == "__main__":
    print()
    print("===**************************************===")
    print("Welcome to the skive Banking Application!")
    print("===**************************************===")
    print()


    while True:
        print("1. Show your balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Exit")
        print()
        print("=========================================")
        choice = input("Enter your choice: ")
        print("=========================================")
        print()

        if choice == "1":
            check_balance()
        elif choice == "2":
            print()
            amt = float(input("Enter the amount to deposit: "))
            deposit(amt)
            print(f"amount deposited: ${amt}. Your balance is: ${balance}")
        elif choice == "3":
            print()
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)
            print(f"amount withdrawn: ${amt}. Your balance is: ${balance}")
        elif choice == "4":
            check_kyc()
        elif choice == "5":
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to upload: "))
            for i in range(n_documents):
                key = input("enter the document type:")
                value = input("enter the document number:")
                kyc_docs[key] = value
            kyc(kyc_docs)
            print()
            print("=========================================")
            print("KYC updated")
            print("=========================================")
            print()
        elif choice == "6":
            print("QUITING")
            break
        else:
            print()
            print("=========================================")
            print("Invalid choice. Please try again.")
            print("=========================================")
            print()

    print()
    print("===**************************************===")
    print("Thank you for using the banking application.")
    print("===**************************************===")