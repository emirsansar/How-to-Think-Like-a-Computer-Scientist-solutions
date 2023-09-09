#Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:

def replace(s, old, new):

    new_list = s.split(old)

    son = new.join(new_list)

    return son

print(replace("Mississippi", "i", "I"))

print(replace("I love spom! Spom is my favorite food. Spom, spom, yum!", "om", "am"))