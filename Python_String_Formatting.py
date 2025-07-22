#F-string allows you to format selected parts of a string.

#Example : Creating an f-string
txt= f"Hello this is Eyasin Arafath form Dhaka"
print(txt)

#output : Hello this is Eyasin Arafath form Dhaka

#Example : using placeholers in f-string
age = input("Enter your age:")
txt = f"You are {age} years old"
print(txt)

#Output : 
"""Enter your age:25
You are 25 years old
"""

#Example : Modifying a placeholder in f-string 
#Method 01:
price = input("Enter your asking price :")
txt1= f"Your asking price is {price} and it is beyound our budget"
txt2= f"Your asking price is {price} and it is within our budget"

if int(price) > 500:
    print(txt1)
else:
    print(txt2)

#Output : 
"""
Enter your asking price :879
Your asking price is 879 and it is beyound our budget
"""

#Method 02:
price_1 = input("Enter your asking price :")
txt3 = f"Your asking price is { "beyound our limit" if int (price_1)> 500 else "within our limit"}"
print(txt3)
