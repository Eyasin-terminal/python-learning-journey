#Today we learn how to take input from the user.

#Example 01:
print("Enter your name :")
name = input()
print(f"Hello ! Great to meet you {name}")

'''Output:
-Enter your name :
-Eyasin
-Hello ! Great to meet you Eyasin'''


#Example 02:
phone_number = input("Please provide a valid phone number:")
print(f"Do you want to confirm {phone_number} as your phone number?")

'''Output:
Please provide a valid phone number:13*******
Do you want to confirm 13******* as your phone number?'''

#Example 03:
name = input("Enter your full name:")
date = input("Enter your travel date")
location= input( "Enter the location you want to visit:")
Duraiton= input("Enter the duration of your tip:")

print(f"Hello {name}! We are sorry to inform you that \n your trip to {location} on {date} for {Duraiton} days is not posssible")

""" Output:
Enter your full name:Godfather
Enter your travel date 7th June
Enter the location you want to visit:Tokyo
Enter the duration of your tip:3 days
Hello Godfather! We are sorry to inform you that 
your trip to Tokyo on  7th June for 3 days days is not posssible"""

print ("Catch you soon again. Goodbye!")
print ("==================================================================")