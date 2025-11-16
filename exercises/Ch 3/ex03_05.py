# 3-5 Changing Guest List 

guest_list = ['dean martin', 'amy winehouse', 'robin williams']

guest_list.insert(-2, 'frank sinatra')

print(f"Hello, {guest_list[0].title()}! I would love to invite you to dinner.")
print(f"Hello, {guest_list[-2].title()}! I would love to invite you to dinner.")
print(f"Hello, {guest_list[-1].title()}! I would love to invite you to dinner.\n")

print(f"Unfortunately, {guest_list.pop(-2).title()} can't make it.\n")

print(f"""Those who are in the list, and can make it:
      {guest_list[0].title()}, {guest_list[1].title()}, and {guest_list[-1].title()}\n""")


