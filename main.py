def add_income():
    amount = float(input("Enter Amount:"))
    description = input("Enter Description:")
    
    
     
    with open("data.txt","a") as file:
        file.write(f"INCOME:{amount} {description}\n")
    print("Income added succesfully.")    
def add_expense():
    amount = float(input("Enter Amount:"))
    description = input("Enter  Description:")
    

    with open("data.txt","a") as file:
        file.write(f"EXPENSE:{amount} {description}\n")
    print("Expense added successfully.")
def show_balance():
    import os 
    if not os.path.exits("data.txt"):
        print("No Transactions found.")
        return
    balance = 0.0 
    with open("data.txt","r") as file:
        for line in file:
            line = line.strip()

            #skip empty lines 
            if not line:
                continue


            parts = line.split(":")
            #skip invalid lines 
            if len(parts) != 2:
                continue
            transaction_type = parts[0]
            details = parts[1]
            
            amount = float(details.split()[0])

            if transaction_type == "INCOME":
             balance += amount
            elif transaction_type == "EXPENSE":
             balance -= amount
        print("current balance:",balance) 
def show_history():
    print("====== Transaction History ======")

    with open ("data.txt","r") as file:

        empty = True

        for line in file:
            line = line.strip()

            # to skip empty lines 
            if not line :
                continue

            parts = line.split(":")
            if len(parts) != 2:
                continue
            transaction_type = parts[0]
            details = parts[1]
            
            print(f"{transaction_type:} : {details}")

            empty = False
        if empty:
            print("no transactions found.")

    print("====================================")           


           
    



def main():
    while True:
       print()
       print("\n======The Expense Tracker====== ")
       print()
       print("1. Add Income")
       print("2. Add Expense")
       print("3. Show Balance")
       print("4. Show History")
       print("5. Exit")
       print("==================================")
    

       choice = (input("Enter your choice:"))
       if choice == "1":
          add_income()
       elif choice == "2":
          add_expense()
       elif choice == "3":
          show_balance()
       elif choice == "4":
          show_history()
       elif choice == "5":
            print("Exited..")
            break  
       else:
          print("invalid choice")
    
if __name__ == "__main__":
        main()