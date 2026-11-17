
# create function with option using While
# 1 deposit
# 2 withdraw

# បង្កើតមុខងារសម្រាប់ដាក់ប្រាក់ (Deposit Function)
def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"Deposit successful! Current Balance: ${balance:.2f}")
    else:
        print("Invalid amount! Amount must be greater than 0.")
    return balance

# បង្កើតមុខងារសម្រាប់ដកប្រាក់ (Withdraw Function)
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient balance!")
    elif amount <= 0:
        print("Invalid amount! Amount must be greater than 0.")
    else:
        balance -= amount
        print(f"Withdrawal successful! Remaining Balance: ${balance:.2f}")
    return balance


while True:
        print("\n=== Welcome to ATM Machine ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        
        option = input("Select an option (1/2/3): ")
        
        if option == "1":
            amount = float(input("Enter amount to deposit: $"))
            balance = deposit(balance, amount)
            
        elif option == "2":
            amount = float(input("Enter amount to withdraw: $"))
            balance = withdraw(balance, amount)
            
        elif option == "3":
            print("Thank you for using our ATM. Goodbye!")
            break
            
        else:
            print("Invalid option! Please choose 1, 2, or 3.")