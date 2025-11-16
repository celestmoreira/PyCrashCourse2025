# 3-6 More Guests

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
