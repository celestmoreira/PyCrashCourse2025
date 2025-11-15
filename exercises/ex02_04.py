# Name Cases 
# Use a variable to represent a person's name, and then print that person's 
# name in lowercase, uppercase, and title case. 
#-----------------------------------------------------------------

# Store the person's name inside a variable.
name = "Celest"

# Using triple quotes for this string so that it can span multiple lines
# without breaking. 
message = f"""This is your name in lowercase:
\t{name.lower()}

This is your name in uppercase:
\t{name.upper()}

This is your name in title case:
\t{name.title()}."""

print(message)
