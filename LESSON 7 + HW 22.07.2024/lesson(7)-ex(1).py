# LESSON 7 EX 1 HW

# STRING BASIC

# Create a single string with your full name and city of residence.
# Make sure there's a space between the names
# 1. Print the length of the string. Hint: len
# 2. Print the entire string in uppercase. Hint: upper
# 3. Print the entire string in lowercase. Hint: lower
# 4. Check if the string starts with your first name. Hint: startswith
# 5. Check if the string ends with your city of residence. Hint: endswith
# 6. Split the string into a list containing your first name, last name, and city of residence. Hint: split
# 7. Replace the spaces with asterisks. Hint: replace. Then split the new string into a list again.
# 8. Print the string centered within 50 characters, wrapped with the "=" character. Hint: center
# 9. Print the string from the 4th character to the end
# 10. Print the string from the beginning to the 4th character (inclusive)
# 11. Print all the even-indexed characters in the string
# 12. Ensure that each word in the string starts with a capital letter. Hint: title

# START

# Create a single string with your full name and city of residence.
# Make sure there's a space between the names
full_string = "Daniel Mizrahi Tel Aviv"

# 1. Print the length of the string. Hint: len
print("Length of the string:", len(full_string))

# 2. Print the entire string in uppercase. Hint: upper
print("Uppercase:", full_string.upper())

# 3. Print the entire string in lowercase. Hint: lower
print("Lowercase:", full_string.lower())

# 4. Check if the string starts with your first name. Hint: startswith
print("Starts with 'Daniel':", full_string.startswith("Daniel"))

# 5. Check if the string ends with your city of residence. Hint: endswith
print("Ends with 'Tel Aviv':", full_string.endswith("Tel Aviv"))

# 6. Split the string into a list containing your first name, last name, and city of residence. Hint: split
split_list = full_string.split()
print("Split list:", split_list)

# 7. Replace the spaces with asterisks. Hint: replace. Then split the new string into a list again.
replaced_string = full_string.replace(" ", "*")
print("Replaced string:", replaced_string)
replaced_split_list = replaced_string.split("*")
print("Split replaced string:", replaced_split_list)

# 8. Print the string centered within 50 characters, wrapped with the "=" character. Hint: center
centered_string = full_string.center(50, "=")
print("Centered string:", centered_string)

# 9. Print the string from the 4th character to the end
print("From the 4th character to the end:", full_string[3:])

# 10. Print the string from the beginning to the 4th character (inclusive)
print("From the beginning to the 4th character:", full_string[:4])

# 11. Print all the even-indexed characters in the string
print("Even-indexed characters:", full_string[::2])

# 12. Ensure that each word in the string starts with a capital letter. Hint: title
print("Title case:", full_string.title())

# END

# Length of the string: 23
# Uppercase: DANIEL MIZRAHI TEL AVIV
# Lowercase: daniel mizrahi tel aviv
# Starts with 'Daniel': True
# Ends with 'Tel Aviv': True
# Split list: ['Daniel', 'Mizrahi', 'Tel', 'Aviv']
# Replaced string: Daniel*Mizrahi*Tel*Aviv
# Split replaced string: ['Daniel', 'Mizrahi', 'Tel', 'Aviv']
# Centered string: =============Daniel Mizrahi Tel Aviv==============
# From the 4th character to the end: iel Mizrahi Tel Aviv
# From the beginning to the 4th character: Dani
# Even-indexed characters: Dne irh e vv
# Title case: Daniel Mizrahi Tel Aviv