# 3-10 Every Function 

shows = ['The Office', 'The Sopranos', 'Malcom in the Middle', 'The Three Stooges',
          'Sam & Cat', 'Better Call Saul', 'Breaking Bad']

print("\n What is the length of the list?")
print(f"\t The length is: {len(shows)}.")

del shows[0]

print("\nNow what's the length?")
print(f"\tThe length is now: {len(shows)}.")

print("\nShow me the orginal list.")
print(f"""\tHere is the orginal list:
       {shows}""")

print("\nShow me the sorted list.")
print(f"""\tHere is the sorted list:
       {sorted(shows)} \n""")