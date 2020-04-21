# Jackson Jared
# 4.21.2020
# This is an assignment using Regular Expressions to search a string for particular characters
import re

# Identifiers
# \d any number
# \D anything but a number
# \s space
# \S anything but a space
# \w any character
# \W anything but a character
# . any character except a new line
# \b the white space around words
# \. period
#
# Modifiers
# {1, 3} expecting 1 - 3
# + match one or more
# * match zero or more
# ^ matches the beginning
# $ matches the end
# ? optional character
# | either or
# [] range or variance
# {x} expecting x amount
#
# White Space Characters
# \n new line
# \s space
# \t tab
# \e escape
# \f form feed
# \r return
#
# DON'T FORGET
# . + * ? [] $ ^ () {} | \

menu = "code"
while menu != "end":
    print("__" * 50)
    string = input("\nType Your String"
                   "\n>>>")
    while menu != 'ending':
        do = input("\n\n(TYPE THE NUMBER NEXT TO THE DESIRED CHOICE)"
                   "\nWhat Would You Wish To DO?"
                   "\n1. See if the string has a 'q'"
                   "\n2. See if the string contains 'the'"
                   "\n3. See if the string has a '*' in it"
                   "\n4. See if the string contains a digit"
                   "\n5. See if the string contains a period"
                   "\n6. See if the string has at least 2 consecutive vowels (a,e,i,o,u) like in the word 'bear'"
                   "\n7. See if the string contains white space"
                   "\n8. See if the string has any letters that repeat three times in a single word"
                   "\n9. See if the string starts with the word ‘Hello’ (must match the capital H)"
                   "\n10. See if the string contains an email address (what is the pattern for an email address?"
                   "\n11. Enter A New String"
                   "\n12. Exit The Program"
                   "\n>>>")
        while do is not None:
            try:
                do = int(do)
                print("")
                break
            except ValueError:
                print("\nEnter a number 1 - 12")
                do = input("\n>>>")

        if do == 11:
            print("Alright")
            break
        if do == 12:
            print("Adios")
            quit()

        if do == 1:
            # 1.See if the string has a 'q'
            find = re.findall(r"\w*[Qq]\w*", string)
            if find:
                print("The string you entered contains at least one q:\n", find)
            else:
                print("The string you entered does not contain a q.")
        if do == 2:
            # 2.See if the string contains 'the'
            if re.search(r"The|the", string):
                print("The string you entered has 'The' or 'the' in it.")
            else:
                print("The string you entered does not have 'The' or 'the' in it.")
        if do == 3:
            # 3.See if the string has a '*' in it
            if re.search(r'[*]', string):
                print('This string contains an \'*\'.')
            else:
                print('This string does not contain an \'*\'.')
        if do == 4:
            # 4.See if the string contains a digit
            find = re.findall(r"\d+", string)
            if find:
                print("The string you enter contains at least one number:\n", find)
            else:
                print("The string you entered does not contain any numbers.")
        if do == 5:
            # 5.See if the string contains a period
            if re.search(r'[.]', string):
                print("This string contains a '.'")
            else:
                print("This string does not contain a '.'")
        if do == 6:
            # 6.See if the string has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear"
            find = re.findall(r'\w*[aeiou][aeiou]\w*', string)
            if find:
                print("This string contains at least one word with 2 consecutive vowels:\n", find)
            else:
                print("This string does not contain any words with 2 consecutive vowels.")
        if do == 7:
            # 7.See if the string contains white space
            if re.search(r'.*\s.*', string):
                print("The string contains a space.")
            else:
                print("This string does not contain a space.")
        if do == 8:
            # 8.See if the string has any letters that repeat three times in a single word
            find = re.findall(r'\w*.{3}\w*', string)  # This is not working as intended
            if find:
                print("This string includes at least one word with a letter that repeats 3 times within that word:\n", find)
            else:
                print("This string does not include a word with a letter that repeats 3 times within that word.")
        if do == 9:
            # 9.See if the string starts with the word ‘Hello’ (must match the capital H)
            if re.search(r'^Hello', string):
                print("This string starts with the word 'Hello'.")
            else:
                print("This string does not start with the word 'Hello'.")
        if do == 10:
            # 10.See if the string contains an email address (what is the pattern for an email address?)
            find = re.findall(r'\w+@\w+\.\w+', string)
            if find:
                print("The string contains at least one email address in it:\n", find)
            else:
                print("The string does not contain any email addresses.")

        input("*Press Enter*")
