# LESSON 7 EX 2 HW

# STRING PART B

# 1. Remove the spaces from both sides of the following string: " day-fun "
# 2. Check if the string "hello" contains only letters. Hint: isalpha
# 3. Check if the string "777" contains only digits. Hint: isdigit
# 4. Check if the string " " contains only spaces. Hint: isspace
# 5. For the list ['A ','J ','N ','I ','N'], create a single string. Hint: join
# 6. For the same list, create a single string with '*' between the characters. A*J*N*I*N. Hint: join
# 7. Ignoring case, check if the letter 'e' appears in the word "hELLo". Hint: in, lower
# 8. Bonus: Get a word from the user, then using comprehension, generate a list containing each letter as an element.
# Each letter should be uppercase. Ignore digits.

# START

# 1. Remove the spaces from both sides of the following string: " day-fun "
trimmed_string = " day-fun ".strip()
print("Trimmed string:", trimmed_string)

# 2. Check if the string "hello" contains only letters. Hint: isalpha
is_alpha = "hello".isalpha()
print("Contains only letters:", is_alpha)

# 3. Check if the string "777" contains only digits. Hint: isdigit
is_digit = "777".isdigit()
print("Contains only digits:", is_digit)

# 4. Check if the string " " contains only spaces. Hint: isspace
is_space = " ".isspace()
print("Contains only spaces:", is_space)

# 5. For the list ['A ','J ','N ','I ','N'], create a single string. Hint: join
char_list = ['A', 'J', 'N', 'I', 'N']
joined_string = "".join(char_list)
print("Joined string:", joined_string)

# 6. For the same list, create a single string with '*' between the characters. A*J*N*I*N. Hint: join
star_joined_string = "*".join(char_list)
print("Joined string with '*':", star_joined_string)

# 7. Ignoring case, check if the letter 'e' appears in the word "hELLo". Hint: in, lower
contains_e = 'e' in "hELLo".lower()
print("Contains 'e':", contains_e)

# 8. Bonus: Get a word from the user, then using comprehension, generate a list containing each letter as an element.
# Each letter should be uppercase. Ignore digits.
user_input = input("Enter a word: ")
uppercase_letters = [char.upper() for char in user_input if char.isalpha()]
print("Uppercase letters list:", uppercase_letters)

# END

# Trimmed string: day-fun
# Contains only letters: True
# Contains only digits: True
# Contains only spaces: True
# Joined string: AJNIN
# Joined string with '*': A*J*N*I*N
# Contains 'e': True
# Enter a word: PYTHON
# Uppercase letters list: ['P', 'Y', 'T', 'H', 'O', 'N']