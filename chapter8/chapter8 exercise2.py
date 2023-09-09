# Modify:
#
# prefixes = "JKLMNOPQ"
# suffix = "ack"
# for letter in prefixes:
# print(letter + suffix)
#
#so that Ouack and Quack are spelled correctly.

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "Q" or letter == "O":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)