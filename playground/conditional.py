phone_balance = 2 
bank_balanace = 100

# IF statement - aslo using hte str() method to convert the int variable phone_balance 
# into a string and rabbit append it into the sentance. 

message = "The phone balance is {} and the bank balance is {}.".format(phone_balance, bank_balanace)
print(message)

print("The phone balance is " + str(phone_balance), "The bank balance is " + str(bank_balanace))

if phone_balance < 5:
    phone_balance += 10
    bank_balanace -= 10 

print("The phone balance is " + str(phone_balance), "The bank balance is " + str(bank_balanace))
