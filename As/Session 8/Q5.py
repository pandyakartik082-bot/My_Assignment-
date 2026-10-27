# 5.
# Create a function mask_phone_number(phone) that takes a 10-digit phone number as a string and returns it in the format '******1234', showing only the last 4 digits like Paytm does.<br><br><em><strong>Hint:</strong> Use string slicing and concatenation.</em>

def mask_phone_number(phone):
    return "******" + phone[-4:]

phone = input("Enter 10-digit phone number: ")

if len(phone) == 10 and phone.isdigit():
    print("Masked Phone Number:", mask_phone_number(phone))
else:
    print("Invalid phone number")