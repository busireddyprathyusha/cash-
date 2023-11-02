balance = 5000
username = "myusername"
password = "mypassword"
operations = ["credit", "debit", "mini statement"]
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
while True:
    if input_username == username and input_password == password:
        print("Login successful!")
        selected_operation = input("Select an operation (credit/debit/mini statement):")
    if selected_operation in operations:
        if selected_operation == "credit":
            credit_amount = int(input("Enter the credit amount: "))
            balance += credit_amount
            print("Amount credited: {credit_amount}, Available balance: {balance}")
        elif selected_operation == "debit":
            debit_amount = int(input("Enter the debit amount: "))
            if debit_amount > balance:
                print("Insufficient balance")
            else:
                balance -= debit_amount
                print(f"Amount debited: {debit_amount}, Available balance: {balance}")
        else:
            print(f"Available balance: {balance}")
    else:
        print("Invalid operation selected")
else:
    print("Invalid username or password")
print(" final available balance")
