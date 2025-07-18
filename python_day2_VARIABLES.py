# Today we learn python variables

name = "Eyasin Arafath"     # string variable (by default)
age = 21                    # integer variable (by default)
country = "Bangladesh"      # string variable (by default)

# printing the variables
print(name)
print(age)
print(type(country))  # printing the type of variable

"""
Now we will solve a real life problem
Project Idea: The Digital Business Card

Problem:
Imagine you're at a networking event, but you've run out of paper business cards. 
You want to quickly send your professional details to a new contact. You can write a simple Python script 
to store your details and print them in a clean, formatted way.

Why this is a real-life problem:
- Data Storage: From phone contacts to social media, variables store & display information.
- Data Presentation: How you present info is key. This script is a display template.
"""

# Solution
# Step 01: Storing the variables
full_name = "Eyasin Arafath"
job_title = "AI Agent"
company_name = "Google"
email = "f4m0H@example.com"
phone_number = "01745678"
website = "www.google.com"

# Step 02: Printing the business card
print("\n--- Digital Business Card ---\n")
print(f"""
----------------------------
| Name: {full_name}
| Title: {job_title}
| Company: {company_name}
| Email: {email}
| Phone: {phone_number}
| Website: {website}
----------------------------
""")
