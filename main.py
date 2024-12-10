# Thayer Yang
# 10 DEC 2024
# Validating String Input (Tiered Assignment)

# Level 1

# run = True
# while run:
#     message = input("Enter a message (type \"-q-\" to quit):\n")

#     if message == "-q-":
#         run = False
#     else:
#         if message.isalpha():
#             print(f"Valid input:\n{message}")
#         else:
#             print("Invalid Input: Enter alphabetical characters only")

# Level 2
            
# run = True
# while run:
#     message = input("Please enter a 5 or longer digit number (type \"-q-\" to quit):\n")

#     if message == "-q-":
#         run = False
#     else:
#         if message.isdigit() and len(message) >=5:
#             print(f"Valid input:\n{message}")
#         elif not message.isdigit():
#             print("Invalid Input: Enter numeric values only")
#         elif len(message) < 5:
#             print("Invalid Input: Input is not at least 5 digits")

# Level 3
            

print("Try to enter 5 valid Strings")
attempts = 0
valid_messages = []
invalid_messages = []
while len(valid_messages) < 5:
    attempts +=1
    message = input("Enter a string: ")

    if (message.isalpha() or message.isdigit()) and (len(message) >=6 and len(message) <= 10):
        print(f"The String is a valid message: {message}")
        valid_messages.append(message)
    else:
        print("This string is not valid.")
        invalid_messages.append(message)
        if not (message.isalpha() or message.isdigit()):
            print("Hint: Try to enter alphabetic or numeric characters (Not Both).")
        elif len(message) > 10 or len(message) < 6:
            print("Hint: Try to stay between 6-10 characters in length.")

print("YOU DID IT!")
print(f"""Attempts: {attempts}
Valid Inputs: {valid_messages}
Invalid Inputs: {invalid_messages}""")