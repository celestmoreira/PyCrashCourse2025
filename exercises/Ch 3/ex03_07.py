# 3-7 Shrinking Guest List 

guest_list = ['dean martin', 'amy winehouse', 'robin williams']

print(f"Hello, {guest_list[0].title()}! I would love to invite you to dinner.")
print(f"Hello, {guest_list[-2].title()}! I would love to invite you to dinner.")
print(f"Hello, {guest_list[-1].title()}! I would love to invite you to dinner.\n")

guest_list.insert(-2, 'frank sinatra')
guest_list.insert(0, 'Sammy Davis Jr.')
guest_list.insert(-1, 'Chris Farley')
guest_list.insert(2, 'Doris Day')

print(f"Unfortunately, {guest_list.pop(-3).title()} can't make it.\n")

print(f"{guest_list[0].title()} will be joining us!")
print(f"{guest_list[1].title()} will be joining us!")
print(f"{guest_list[2].title()} will be joining us!")
print(f"{guest_list[3].title()} will be joining us!")
print(f"{guest_list[-2].title()} will be joining us!")
print(f"{guest_list[-1].title()} will be joining us!\n")

print("Hello everyone! Turns out I can only invite two people. :(\n")

print(f"Sorry, {guest_list.pop(0).title()} I can't invite you to dinner.")
print(f"Sorry, {guest_list.pop(3).title()}, I can't invite you to dinner.")
print(f"Sorry, {guest_list.pop(-2).title()}, I can't invite you to dinner.")
print(f"Sorry, {guest_list.pop(-1).title()}, I can't invite you to dinner.\n")

print(f"Only {guest_list[0].title()} and {guest_list[1].title()} will be joining me!\n")

del guest_list[0]
del guest_list[0]

print(guest_list)