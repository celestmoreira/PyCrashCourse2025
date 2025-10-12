first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # use f strings to insert a variable's value into a string.
print(full_name)

# --- you can use f-strings to compose complete messages using the info associated with a variable --- 
print(f"Hello, {full_name.title()}!") # .title() changes output to title case

#---you can also use f-strings to compose a message and assign the entire message to a variable---
message = f"Hello, {full_name.title()}!"
print(message)

