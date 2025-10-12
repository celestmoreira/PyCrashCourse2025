print("Python") # no whitespace 
print("\tPython") # to add a tab to your text use \t
print("Languages:\nPython\nC\nJacaScript") # to add a newline in a string, use \n
print("Languages:\n\tPython\n\tC\n\tJavaScript") # to combine tabs and newlines 

#---STRIPPING WHITESPACE---
favorite_language = 'python ' # extra whitespace after python
favorite_language.rstrip()    # use the .rstrip() method to strip any whitespace 
print(favorite_language)      # HOWEVER this is temporary to make permanent see below

favorite_language = favorite_language.rstrip() # associate the stripped value with the variable name to make permanent
print(favorite_language)

#--- you can also strip whitespace from the left side of a string using lstrip() method, or from both sides at once using strip().
favorite_language = " python "
favorite_language.rstrip() # prints " python"
favorite_language.lstrip() # prints "python "
favorite_language.strip()  # prints "python"
