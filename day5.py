#Function

def business_card(name: str, title: str, company: str, email: str, phone: str, website: str) -> None:
    """
    Generates and prints a formatted business card to the console.
    """
    # The following lines are now indented, making them part of the function.
    card = f"""
    =========================
    Name: {name}
    Title: {title}
    Company: {company}
    Email: {email}
    Phone: {phone}
    Website: {website}
    =========================
    """
    print(card)


"""OUTPUT:
 =========================
    Name: Eyasin Arafath
    Title: AI Agent
    Company: Google
    Email: f4m0H@example.com
    Phone: 01745678
    Website: www.google.com
    ========================="""

print()
business_card(
    name="Eyasin Arafath",
    title="AI Agent",
    company="Google",
    email="f4m0H@example.com",
    phone="01745678",
    website="www.google.com"
)

